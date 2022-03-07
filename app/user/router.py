

from typing import List
from sqlalchemy.orm import Session
from app import db

from . import schema
from . import validator as UserValidator
from . import services as UserService

from fastapi import APIRouter, Depends, HTTPException, Response, status

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
   
    user = await UserValidator.verify_email_exist(request.email, database)
    
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system."
            )
    
    new_user = await UserService.new_user_register(request, database)
    return new_user

@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await UserService.all_users(database)

@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await UserService.get_user_by_id(user_id, database)

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await UserService.delete_user_by_id(user_id, database)