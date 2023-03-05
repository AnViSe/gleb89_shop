from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import Categoriesservice, get_categories_service
from . import schema

app = APIRouter(prefix='/api/v1/categories',tags=['Категории'])


@app.get(
        '/',
        summary='Список',
         response_model=List[schema.CategoryInfo]
         )
async def list(
    limit:Optional[int] = 60,
    service:Categoriesservice = Depends(get_categories_service)
    ):
    return await service.get_list(limit)


@app.get(
        '/{id}',
        summary='Один item',
        response_model=schema.CategoryInfo)
async def get_one(
    id:int,
    service:Categoriesservice = Depends(get_categories_service)
    ):
    return await service.get_one(id)


@app.post('/',summary='Создание',status_code=201)
async def create(
    data:schema.CategoryCreateUpdate,
    service:Categoriesservice = Depends(get_categories_service)
    ):
    return await service.create(data)

@app.delete('/{id}',summary='Удаление')
async def delete(
    id:int,
    service:Categoriesservice = Depends(get_categories_service)
    ):
    return await service.delete(id)