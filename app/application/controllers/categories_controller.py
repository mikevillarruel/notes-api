from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.di import get_categories_service
from app.domain.interfaces import ICategoriesService
from app.domain.models import CategoryIn, CategoryOut

categories_router = APIRouter()


@categories_router.get("/", response_model=list[CategoryOut])
def get(service: ICategoriesService = Depends(get_categories_service)):
    try:
        return service.get()
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@categories_router.get("/{category_id}", response_model=CategoryOut)
def get_by_id(category_id: int, service: ICategoriesService = Depends(get_categories_service)):
    try:
        return service.get_by_id(category_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@categories_router.post("/", response_model=CategoryOut)
def add(note: CategoryIn, service: ICategoriesService = Depends(get_categories_service)):
    try:
        return service.add(note)
    except Exception as e:
        return HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@categories_router.put("/{category_id}", response_model=CategoryOut)
def update(category_id: int, note: CategoryIn, service: ICategoriesService = Depends(get_categories_service)):
    try:
        return service.update(category_id, note)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )


@categories_router.delete("/{category_id}", response_model=CategoryOut)
def delete(category_id: int, service: ICategoriesService = Depends(get_categories_service)):
    try:
        return service.delete(category_id)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.EXPECTATION_FAILED,
            detail=e.__str__()
        )
