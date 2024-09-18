from abc import ABC, abstractmethod

from app.domain.models import CategoryOut, NoteIn, NoteOut


class INotesService(ABC):

    @abstractmethod
    def get(self, filters: dict) -> list[NoteOut]:
        pass

    @abstractmethod
    def get_by_id(self, note_id: int) -> NoteOut:
        pass

    @abstractmethod
    def add(self, note: NoteIn) -> NoteOut:
        pass

    @abstractmethod
    def update(self, note_id: int, note: NoteIn) -> NoteOut:
        pass

    @abstractmethod
    def delete(self, note_id: int) -> NoteOut:
        pass

    @abstractmethod
    def add_category(self, note_id: int, category_id: int) -> NoteOut:
        pass

    @abstractmethod
    def remove_category(self, note_id: int, category_id: int) -> NoteOut:
        pass

    @abstractmethod
    def get_categories(self, note_id: int) -> list[CategoryOut]:
        pass

    @abstractmethod
    def toggle_is_archived(self, note_id: int) -> NoteOut:
        pass
