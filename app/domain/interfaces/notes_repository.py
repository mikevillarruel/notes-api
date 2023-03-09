from abc import ABC, abstractmethod

from app.domain.models import Note, NoteCreation, NoteUpdate


class INotesRepository(ABC):

    @abstractmethod
    def get(self) -> list[Note]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Note:
        pass

    @abstractmethod
    def add(self, note: NoteCreation) -> Note:
        pass

    @abstractmethod
    def update(self, id: int, note: NoteUpdate) -> Note:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
