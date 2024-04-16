# Simple User Registration API

This project implements a simple User Registration API using FastAPI and MySQL.

## Setting up the SQL Server

1. **Install MySQL Server**: Install MySQL Server on your machine if you haven't already. You can download it from [here](https://dev.mysql.com/downloads/).

2. **Create Database**: You need to create a MySQL database for the application. You can do this using a MySQL client like MySQL Workbench or through command line:

    ```sql
    CREATE DATABASE users;
    ```
   ***Note.***  Step 2 is optional a new database will be created with the name ```users``` if not available once the project starts running.

3. **Database Configuration**: Update the `database_config.py` file with your MySQL database configuration:

    ```python
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "your_password",
        "database": "users",
    }
    ```

## Installing Dependencies

1. **Create Virtual Environment**: It's a good practice to use a virtual environment for Python projects. You can create one using `venv`:

    ```bash
    python -m venv venv
    ```

2. **Activate Virtual Environment**: Activate the virtual environment. On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```

3. **Install Requirements**: Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Run FastAPI Server**: Start the FastAPI server by running the following command:

    ```bash
    uvicorn main:app --reload
    ```

2. **Access API Documentation**: Once the server is running, you can access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- **Register User**: `POST /auth/register` - Register a new user with a name, username, email, and password.
- **Login**: `POST /auth/login` - Authenticate and login a user.
