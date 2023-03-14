from sqlalchemy import Table, Column, Integer, String, Float
from config.db import meta

stud = Table(
    "stud", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("address", String(255)),
    Column("marks", Float)
)