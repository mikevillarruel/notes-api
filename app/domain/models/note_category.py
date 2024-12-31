from sqlalchemy import Column, ForeignKey, Table

from .base import Base

NoteCategory = Table(
    "note_category",
    Base.metadata,
    Column("note_id", ForeignKey("note.id"), primary_key=True),
    Column("category_id", ForeignKey("category.id"), primary_key=True),
)
