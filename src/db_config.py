import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from logger import ProjectLogger
from pathlib import Path

# Setup logging


def sql_engine():
    """
    Return a SQLAlchemy engine object using the database credentials set in
    the environment variables.

    The environment variables used are:

    - DB_USER: the username to use for the database connection
    - DB_PASSWORD: the password to use for the database connection
    - DB_HOST: the hostname of the database server
    - DB_PORT: the port number to use for the database connection
      (default is 3306)
    - DB_NAME: the name of the database to connect to

    If any of the environment variables are not set, a message will be printed
    to the console.

    Returns:
        A SQLAlchemy engine object, or None if the connection fails.
    """
    env_path = Path(__file__).resolve().parent.parent / 'src' / 'conf.env'

# Load it explicitly
    loaded = load_dotenv(dotenv_path=env_path)
    print(f".env loaded: {loaded}")
    log=ProjectLogger()
    db_credentials = {
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASSWORD"),
        'host': os.getenv("DB_HOST"),
        'port': os.getenv("DB_PORT", '3306'),  # default port 3306
        'database': os.getenv("DB_NAME"),
    }
    #for key, value in db_credentials.items():
     #    if value is None:
      #      print(f"Environment variable {key.upper()} is not set.")
    # Build the connection URL
    """
    makes the connection to the database
    """
    connection_url = (
        f"mysql+pymysql://{db_credentials['user']}:{db_credentials['password']}"
        f"@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['database']}"
    )

    try:
        engine = create_engine(connection_url)
        log.info("Database connection successful.")
        return engine
    except Exception as e:
        log.error(f"Database connection failed: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    engine = sql_engine()
