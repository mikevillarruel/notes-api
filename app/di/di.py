from app.domain.services import CategoriesService, NotesService
from app.infrastructure.db_connector import POSTGRESQL
from app.infrastructure.repositories import (CategoriesRepository,
                                             NotesRepository)


def get_notes_repository():
    return NotesRepository(
        POSTGRESQL.get_instance()
    )


def get_notes_service():
    return NotesService(
        get_notes_repository()
    )


def get_categories_repository():
    return CategoriesRepository(
        POSTGRESQL.get_instance()
    )


def get_categories_service():
    return CategoriesService(
        get_categories_repository()
    )
