from app.domain.services import NotesService
from app.infrastructure.repositories import NotesRepository


def get_note_service() -> NotesService:
    return NotesService(
        get_posgresql_repository()
    )


def get_posgresql_repository() -> NotesRepository:
    return NotesRepository()
