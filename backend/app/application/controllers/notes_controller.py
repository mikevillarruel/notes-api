from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from app.di import get_notes_service
from app.domain.interfaces import INotesService
from app.domain.models import CategoryOut, NoteIn, NoteOut

notes_router = APIRouter()


@notes_router.get("/", response_model=list[NoteOut])
def get(
        is_archived: bool = Query(None, description="Filter by is_archived"),
        category_id: int = Query(None, description="Filter by category_id"),
        service: INotesService = Depends(get_notes_service)
):
    try:
        filters = {
            "is_archived": is_archived,
            "category_id": category_id,
        }
        filters = {k: v for k, v in filters.items() if v is not None}
        return service.get(filters)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.get("/{note_id}", response_model=NoteOut)
def get_by_id(note_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.get_by_id(note_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.post("/", response_model=NoteOut)
def add(note: NoteIn, service: INotesService = Depends(get_notes_service)):
    try:
        return service.add(note)
    except Exception as e:
        return HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.put("/{note_id}", response_model=NoteOut)
def update(note_id: int, note: NoteIn, service: INotesService = Depends(get_notes_service)):
    try:
        return service.update(note_id, note)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.delete("/{note_id}", response_model=NoteOut)
def delete(note_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.delete(note_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.post("/{note_id}/categories/{category_id}", response_model=NoteOut)
def add_category(note_id: int, category_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.add_category(note_id, category_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.delete("/{note_id}/categories/{category_id}", response_model=NoteOut)
def remove_category(note_id: int, category_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.remove_category(note_id, category_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.get("/{note_id}/categories", response_model=list[CategoryOut])
def get_categories(note_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.get_categories(note_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@notes_router.put("/{note_id}/toggle_is_archived", response_model=NoteOut)
def toggle_is_archived(note_id: int, service: INotesService = Depends(get_notes_service)):
    try:
        return service.toggle_is_archived(note_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )
