from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.di import get_note_service
from app.domain.interfaces import INotesService
from app.domain.models import Note, NoteCreation, NoteUpdate

notes_router = APIRouter()


@notes_router.get("/", response_model=list[Note])
def get(service: INotesService = Depends(get_note_service)) -> list[Note]:
    return service.get()


@notes_router.get("/{id}", response_model=Note | dict)
def get_by_id(id: int, service: INotesService = Depends(get_note_service)) -> Note | dict:
    note = service.get_by_id(id)
    if note:
        return note
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")


@notes_router.post("/", response_model=Note)
def add(note: NoteCreation, service: INotesService = Depends(get_note_service)) -> Note:
    return service.add(note)


@notes_router.put("/{id}", response_model=Note)
def update(id: int, note: NoteUpdate, service: INotesService = Depends(get_note_service)) -> Note:
    note = service.update(id, note)
    if note:
        return note
    else:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")


@notes_router.delete("/{id}", response_model=dict)
def delete(id: int, service: INotesService = Depends(get_note_service)) -> dict:
    return {
        "is_deleted": service.delete(id)
    }
