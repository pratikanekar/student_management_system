from fastapi import APIRouter
from config.db import conn
from models.index import stud
from schemas.index import Student

user = APIRouter()


@user.get("/all info", tags=["View Students"])
async def read_data():
    return conn.execute(stud.select()).fetchall()


@user.get("/info by id", tags=["View Students"])
async def read_data(id: int):
    return conn.execute(stud.select().where(stud.c.id == id)).fetchall()


@user.post("/add new student", tags=["Manage Students"])
async def read_data(user: Student):
    conn.execute(stud.insert().values(
        name=user.name,
        email=user.email,
        address=user.address,
        marks=user.marks
    ))
    return conn.execute(stud.select()).fetchall()


@user.put("/update info", tags=["Manage Students"])
async def read_data(id: int, user: Student):
    conn.execute(stud.update().values(
        name=user.name,
        email=user.email,
        address=user.address,
        marks=user.marks
    ).where(stud.c.id == id))
    return conn.execute(stud.select()).fetchall()


@user.delete("/delete student", tags=["Manage Students"])
async def read_data(id: int):
    conn.execute(stud.delete().where(stud.c.id == id))
    return conn.execute(stud.select()).fetchall()
