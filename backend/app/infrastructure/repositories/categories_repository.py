from app.domain.interfaces import ICategoriesRepository
from app.domain.models import CategoryEntity, CategoryIn, CategoryOut
from app.infrastructure.db_connector import DB


class CategoriesRepository(ICategoriesRepository):

    def __init__(self, db: DB):
        self.db = db

    def get(self) -> list[CategoryOut]:
        categories = self.db.session \
            .query(CategoryEntity) \
            .order_by(CategoryEntity.id) \
            .all()
        categories = [category.to_model() for category in categories]
        return categories

    def get_by_id(self, category_id: int) -> CategoryOut:
        category = self.db.session.get(CategoryEntity, category_id)

        if not category:
            raise Exception("Item not found")

        return category.to_model()

    def add(self, category: CategoryIn) -> CategoryOut:
        category_entity = category.to_entity()

        self.db.session.add(category_entity)
        self.db.session.commit()

        return category_entity.to_model()

    def update(self, category_id: int, category: CategoryIn) -> CategoryOut:
        category_entity = self.db.session \
            .query(CategoryEntity) \
            .filter(CategoryEntity.id == category_id) \
            .first()

        if not category_entity:
            raise Exception("Item not found")

        category_entity.name = category.name

        self.db.session.commit()

        return category_entity.to_model()

    def delete(self, category_id: int) -> CategoryOut:
        category_entity = self.db.session \
            .query(CategoryEntity) \
            .filter(CategoryEntity.id == category_id) \
            .first()

        if not category_entity:
            raise Exception("Item not found")

        self.db.session.delete(category_entity)
        self.db.session.commit()

        return category_entity.to_model()
