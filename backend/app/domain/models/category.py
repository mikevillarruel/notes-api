from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .note_category import NoteCategory


class CategoryEntity(Base):
    __tablename__ = "category"

    name: Mapped[str] = mapped_column()
    notes: Mapped[list["NoteEntity"]] = relationship(
        secondary=NoteCategory,
        back_populates="categories",
    )

    def to_model(self):
        return CategoryOut(
            id=self.id,
            name=self.name,
        )


class CategoryIn(BaseModel):
    name: str

    def to_entity(self) -> CategoryEntity:
        return CategoryEntity(
            name=self.name,
        )


class CategoryOut(BaseModel):
    id: Optional[int] = None
    name: str

    def to_entity(self) -> CategoryEntity:
        return CategoryEntity(
            id=self.id,
            name=self.name,
        )
