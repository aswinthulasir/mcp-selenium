from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import settings
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

class Person(BaseModel):
    name: str
    age: int

def get_connection():
    return psycopg2.connect(
        host=settings.database_hostname,
        database=settings.database_name,
        user=settings.database_username,
        password=settings.database_password,
        port=settings.database_port,
        cursor_factory=RealDictCursor
    )

@router.post("/add-person")
def add_person(person: Person):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Insert name and get generated ID
        cursor.execute(
            "INSERT INTO name_input (name) VALUES (%s) RETURNING id;",
            (person.name,)
        )
        person_id = cursor.fetchone()['id']

        # Insert age using the same ID
        cursor.execute(
            "INSERT INTO age (id, age) VALUES (%s, %s);",
            (person_id, person.age)
        )

        conn.commit()
        return {"message": "Person added", "id": person_id}

    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()
