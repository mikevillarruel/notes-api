from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.domain.models import Base
from app.utils.env_config import EnvConfig


class DB:
    DB_URL: str = None
    instance: any = None
    session: Session = None

    def __init__(self):
        if not self.DB_URL:
            raise ValueError("DB_URL can't be empty")
        engine = create_engine(self.DB_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance


class POSTGRESQL(DB):
    DB_URL = EnvConfig.DB_URL
