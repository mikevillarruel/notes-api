from sqlalchemy import create_engine, MetaData

from app.utils.env_config import EnvConfig


class DB:
    DB_URL = EnvConfig.DB_URL

    def __init__(self):
        self.engine = create_engine(self.DB_URL)
        self.meta = MetaData()
        self.conn = self.engine.connect()
