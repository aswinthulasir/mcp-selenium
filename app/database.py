from pydantic_settings import BaseSettings
import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor

class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_name: str = "test"
    database_username: str = "postgres"
    database_password: str = "Aswin2000"
    

settings = Settings()

def test_conn():
    conn = None
    try:
        conn = psycopg2.connect(
            host=settings.database_hostname,
            database=settings.database_name,
            user=settings.database_username,
            password=settings.database_password,
            port=settings.database_port
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.fetchone()
        print("Database connection successful.")
    except OperationalError as e:
        print(f"Database connection failed: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()