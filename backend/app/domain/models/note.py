from pydantic import BaseModel
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

    def to_model(self):
        return NoteOut(
            id=self.id,
            title=self.title,
            content=self.content,
            is_archived=self.is_archived,
        )


class NoteIn(BaseModel):
    title: str
    content: str

    def to_entity(self) -> NoteEntity:
        return NoteEntity(
            title=self.title,
            content=self.content,
        )


class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    is_archived: bool

    def to_entity(self) -> NoteEntity:
        return NoteEntity(
            id=self.id,
            title=self.title,
            content=self.content,
            is_archived=self.is_archived,
        )
