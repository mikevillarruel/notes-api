from app.domain.interfaces import INotesRepository, INotesService
from app.domain.models import Note, NoteCreation, NoteUpdate


class NotesService(INotesService):

    def __init__(self, repository: INotesRepository):
        self.repository = repository

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get(self) -> list[Note]:
        return self.repository.get()

    def add(self, note: NoteCreation) -> Note:
        return self.repository.add(note)

    def update(self, id: int, note: NoteUpdate) -> Note:
        return self.repository.update(id, note)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
