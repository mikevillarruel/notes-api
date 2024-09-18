from app.domain.interfaces import ICategoriesRepository, ICategoriesService
from app.domain.models import CategoryIn, CategoryOut


class CategoriesService(ICategoriesService):
    def __init__(self, repository: ICategoriesRepository):
        self.repository = repository

    def get(self) -> list[CategoryOut]:
        return self.repository.get()

    def get_by_id(self, note_id: int) -> CategoryOut:
        return self.repository.get_by_id(note_id)

    def add(self, note: CategoryIn) -> CategoryOut:
        return self.repository.add(note)

    def update(self, note_id: int, note: CategoryIn) -> CategoryOut:
        return self.repository.update(note_id, note)

    def delete(self, note_id: int) -> CategoryOut:
        return self.repository.delete(note_id)
