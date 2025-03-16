from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    name: str | None = Field(default=None)
    
class ToDoList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: str
    status: int | None = Field(default=0)
    score: int = Field(default=0)
    author: str | None = Field(default=None)
    completed_Time: str | None = Field(default=None)
    link: str | None = Field(default=None)