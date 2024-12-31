from typing import Optional

from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .note import NoteOut
from .note_category import NoteCategory


class CategoryEntity(Base):
    __tablename__ = "category"

    name: Mapped[str] = mapped_column()
    notes: Mapped[list["NoteEntity"]] = relationship(
        secondary=NoteCategory,
        back_populates="categories",
    )


class CategoryIn(BaseModel):
    name: str


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    name: str
    notes: list[NoteOut] = []
