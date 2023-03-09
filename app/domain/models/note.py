from pydantic import BaseModel


class Note(BaseModel):
    id: int
    title: str
    content: str
    active: bool


class NoteCreation(BaseModel):
    title: str
    content: str
    active: bool | None


class NoteUpdate(BaseModel):
    title: str | None
    content: str | None
    active: bool | None
