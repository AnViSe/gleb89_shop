from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from apps.base_repo.base_class import BaseService
from .models import Categories
from config.settings import get_session


class Categoriesservice(BaseService[Categories]):

    def __init__(self, db_session:Session):
        super(Categoriesservice,self).__init__(Categories,db_session)



def get_categories_service(db_session:AsyncSession = Depends(get_session))-> Categoriesservice:
    return Categoriesservice(db_session)   