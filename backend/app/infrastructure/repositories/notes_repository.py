from app.domain.interfaces import INotesRepository
from app.domain.models import (CategoryEntity, CategoryOut, NoteEntity, NoteIn,
                               NoteOut)
from app.infrastructure.db_connector import DB


class NotesRepository(INotesRepository):

    def __init__(self, db: DB):
        self.db = db

    def get(self, filters: dict) -> list[NoteOut]:
        category_id = filters.pop("category_id", None)
        notes = self.db.session \
            .query(NoteEntity) \
            .order_by(NoteEntity.id) \
            .filter_by(**filters) \
            .all()
        if category_id:
            notes = [
                note for note in notes
                if category_id in [category.id for category in note.categories]
            ]
        notes = [note.to_model() for note in notes]
        return notes

    def get_by_id(self, note_id: int) -> NoteOut:
        note = self.db.session.get(NoteEntity, note_id)

        if not note:
            raise Exception("Item not found")

        return note.to_model()

    def add(self, note: NoteIn) -> NoteOut:
        note_entity = note.to_entity()

        self.db.session.add(note_entity)
        self.db.session.commit()

        return note_entity.to_model()

    def update(self, note_id: int, note: NoteIn) -> NoteOut:
        note_entity = self.db.session \
            .query(NoteEntity) \
            .filter(NoteEntity.id == note_id) \
            .first()

        if not note_entity:
            raise Exception("Item not found")

        note_entity.title = note.title
        note_entity.content = note.content

        self.db.session.commit()

        return note_entity.to_model()

    def delete(self, note_id: int) -> NoteOut:
        note_entity = self.db.session \
            .query(NoteEntity) \
            .filter(NoteEntity.id == note_id) \
            .first()

        if not note_entity:
            raise Exception("Item not found")

        self.db.session.delete(note_entity)
        self.db.session.commit()

        return note_entity.to_model()

    def add_category(self, note_id: int, category_id: int) -> NoteOut:
        note_entity = self.db.session.get(NoteEntity, note_id)
        category_entity = self.db.session.get(CategoryEntity, category_id)

        if not category_entity or not note_entity:
            raise Exception("Item not found")

        if category_entity in note_entity.categories:
            raise Exception("Category already added to note")

        note_entity.categories.append(category_entity)

        self.db.session.commit()

        return note_entity.to_model()

    def remove_category(self, note_id: int, category_id: int) -> NoteOut:
        note_entity = self.db.session.get(NoteEntity, note_id)
        category_entity = self.db.session.get(CategoryEntity, category_id)

        if not category_entity or not note_entity:
            raise Exception("Item not found")

        if category_entity not in note_entity.categories:
            raise Exception("Category not added to note")

        note_entity.categories.remove(category_entity)

        self.db.session.commit()

        return note_entity.to_model()

    def get_categories(self, note_id: int) -> list[CategoryOut]:
        note_entity = self.db.session.get(NoteEntity, note_id)

        if not note_entity:
            raise Exception("Item not found")

        categories = [category_entity.to_model()
                      for category_entity in note_entity.categories]

        return categories

    def toggle_is_archived(self, note_id: int) -> NoteOut:
        note_entity = self.db.session \
            .query(NoteEntity) \
            .filter(NoteEntity.id == note_id) \
            .first()

        if not note_entity:
            raise Exception("Item not found")

        note_entity.is_archived = not note_entity.is_archived

        self.db.session.commit()

        return note_entity.to_model()
