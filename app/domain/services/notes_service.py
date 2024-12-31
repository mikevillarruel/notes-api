from app.domain.interfaces import INotesRepository, INotesService
from app.domain.models import CategoryOut, NoteIn, NoteOut


class NotesService(INotesService):
    def __init__(self, repository: INotesRepository):
        self.repository = repository

    def get(self, filters: dict) -> list[NoteOut]:
        return self.repository.get(filters)

    def get_by_id(self, note_id: int) -> NoteOut:
        return self.repository.get_by_id(note_id)

    def add(self, note: NoteIn) -> NoteOut:
        return self.repository.add(note)

    def update(self, note_id: int, note: NoteIn) -> NoteOut:
        return self.repository.update(note_id, note)

    def delete(self, note_id: int) -> NoteOut:
        return self.repository.delete(note_id)

    def add_category(self, note_id: int, category_id: int) -> NoteOut:
        return self.repository.add_category(note_id, category_id)

    def remove_category(self, note_id: int, category_id: int) -> NoteOut:
        return self.repository.remove_category(note_id, category_id)

    def get_categories(self, note_id: int) -> list[CategoryOut]:
        return self.repository.get_categories(note_id)

    def toggle_is_archived(self, note_id: int) -> NoteOut:
        return self.repository.toggle_is_archived(note_id)
