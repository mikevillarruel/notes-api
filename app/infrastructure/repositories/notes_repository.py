from sqlalchemy import Boolean, Column, Integer, String, Table

from app.domain.interfaces import INotesRepository
from app.domain.models import Note, NoteCreation, NoteUpdate
from app.infrastructure.db_connector import DB


class NotesRepository(INotesRepository):

    def __init__(self):
        self.db = DB()
        self.note = Table(
            'note',
            self.db.meta,
            Column('id', Integer, primary_key=True),
            Column('title', String(64)),
            Column('content', String(256)),
            Column('active', Boolean, default=True),
            extend_existing=True
        )
        self.db.meta.create_all(self.db.engine)

    def get(self) -> list[Note]:
        result = self.db.conn.execute(self.note.select().order_by('id')).all()
        my_list: list[Note] = []
        for item in result:
            my_list.append(Note(**item._asdict()))
        return my_list

    def get_by_id(self, id: int) -> Note:
        result = self.db.conn.execute(
            self.note.select().where(self.note.c.id == id)
        ).first()
        return Note(**result._asdict()) if result else None

    def add(self, note: NoteCreation) -> Note:
        result = self.db.conn.execute(
            self.note.insert().values(note.dict(exclude_unset=True))
        ).inserted_primary_key[0]
        self.db.conn.commit()
        return self.get_by_id(result)

    def update(self, id: int, note: NoteUpdate) -> Note:
        result = self.db.conn.execute(
            self.note.update().where(self.note.c.id == id).values(note.dict(exclude_unset=True))
        )
        self.db.conn.commit()
        return self.get_by_id(id)

    def delete(self, id: int) -> bool:
        result = self.db.conn.execute(self.note.delete().where(self.note.c.id == id))
        self.db.conn.commit()
        return result.rowcount > 0
