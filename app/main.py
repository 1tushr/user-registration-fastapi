from fastapi import FastAPI
from routes.routers import authrouter
from db.database import create_database_users, create_user_table

app = FastAPI()

# Establish database connection
create_database_users()
create_user_table()

# Include the auth router
app.include_router(authrouter, prefix="/auth", tags=["Authentication"])
