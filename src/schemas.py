from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    createdAt: str
    updatedAt: str

    class config:
        orm_mode = True
        