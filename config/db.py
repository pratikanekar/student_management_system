from sqlalchemy import create_engine, MetaData
from os import getcwd

engine = create_engine(f"sqlite:///{getcwd()}/student.db")
meta = MetaData()
conn = engine.connect()