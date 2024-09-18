from abc import ABC, abstractmethod

from app.domain.models import CategoryIn, CategoryOut


class ICategoriesRepository(ABC):

    @abstractmethod
    def get(self) -> list[CategoryOut]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> CategoryOut:
        pass

    @abstractmethod
    def add(self, category: CategoryIn) -> CategoryOut:
        pass

    @abstractmethod
    def update(self, category_id: int, category: CategoryIn) -> CategoryOut:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> CategoryOut:
        pass
