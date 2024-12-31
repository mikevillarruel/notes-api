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
        categories = [CategoryOut.model_validate(category) for category in categories]
        return categories

    def get_by_id(self, category_id: int) -> CategoryOut:
        category = self.db.session.get(CategoryEntity, category_id)

        if not category:
            raise Exception("Item not found")

        return CategoryOut.model_validate(category)

    def add(self, category: CategoryIn) -> CategoryOut:
        category_entity = CategoryEntity(name=category.name)

        self.db.session.add(category_entity)
        self.db.session.commit()

        return CategoryOut.model_validate(category_entity)

    def update(self, category_id: int, category: CategoryIn) -> CategoryOut:
        category_entity = self.db.session \
            .query(CategoryEntity) \
            .filter(CategoryEntity.id == category_id) \
            .first()

        if not category_entity:
            raise Exception("Item not found")

        category_entity.name = category.name

        self.db.session.commit()

        return CategoryOut.model_validate(category_entity)

    def delete(self, category_id: int) -> CategoryOut:
        category_entity = self.db.session \
            .query(CategoryEntity) \
            .filter(CategoryEntity.id == category_id) \
            .first()

        if not category_entity:
            raise Exception("Item not found")

        self.db.session.delete(category_entity)
        self.db.session.commit()

        return CategoryOut.model_validate(category_entity)
