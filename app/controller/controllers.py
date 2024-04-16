from fastapi import HTTPException, status
from passlib.context import CryptContext
from models.schemas import UserRegistration, UserLogin

# using bcrypt for hashing the password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Logic for registering the user
async def register_user(user: UserRegistration, mycursor, mydb):
    try:
        if not user.name:
            raise HTTPException(status_code=400, detail="Name is required")

        if not user.username or not user.email:
            raise HTTPException(
                status_code=400, detail="Username or Email not provided"
            )

        if user.password != user.confirm_password:
            raise HTTPException(
                status_code=400, detail="Password and confirm password do not match"
            )

        mycursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
        existing_user = mycursor.fetchone()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        mycursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
        existing_email = mycursor.fetchone()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

        hashed_password = pwd_context.hash(user.password)

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        val = (user.username, user.email, hashed_password)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
        registered_user = mycursor.fetchone()

        return {
            "message": "User registered successfully",
            "user": registered_user,
            "status": status.HTTP_201_CREATED,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Logic for logging in the user
async def login_user(user: UserLogin, mycursor, mydb):
    try:
        if not user.username_email or not user.password:
            raise HTTPException(
                status_code=400, detail="Username/Email or Password not provided"
            )
        # Checking if user is entering the username or email to login
        is_email = "@" in user.username_email
        if is_email:
            mycursor.execute(
                "SELECT * FROM users WHERE email = %s", (user.username_email,)
            )
        else:
            mycursor.execute(
                "SELECT * FROM users WHERE username = %s", (user.username_email,)
            )
        db_user = mycursor.fetchone()

        if db_user:
            hashed_password = db_user[3]
            user_details = {
                "id": db_user[0],
                "username": db_user[1],
                "email": db_user[2],
            }
            if pwd_context.verify(user.password, hashed_password):
                return {
                    "message": "Login successfull",
                    "user": user_details,
                    "status": status.HTTP_200_OK,
                }

            else:
                raise HTTPException(status_code=401, detail="Invalid password")
        else:
            raise HTTPException(status_code=401, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
