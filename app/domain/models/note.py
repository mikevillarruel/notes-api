from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .note_category import NoteCategory


class NoteEntity(Base):
    __tablename__ = "note"

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    is_archived: Mapped[bool] = mapped_column(default=False)
    categories: Mapped[list["CategoryEntity"]] = relationship(
        secondary=NoteCategory,
        back_populates="notes",
    )


class NoteIn(BaseModel):
    title: str
    content: str


class NoteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    is_archived: bool
