from fastapi import FastAPI
from app.database import test_conn


from app.routers import add_person

app=FastAPI()
app.include_router(add_person.router)

test_conn()

