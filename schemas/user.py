from pydantic import BaseModel

class Student(BaseModel):
    name: str
    email: str
    address: str
    marks: float