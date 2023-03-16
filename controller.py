from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from core.authentication import JWTBearer
from core.database import get_db
from modules.Users.entity import Manage
from modules.Users.model import Users

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('{/Users}')
def gets(item: Users, db: Session = Depends(get_db)):
    return db.query(manage).all()


@router.get('{/User_id}')
def get(item_id: int,item: Users,  db: Session = Depends(get_db)):
    item = db.query(manage).filter(manage.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return user


@router.post('{/User}')
def create(item: Users, db: Session = Depends(get_db), auth_id: str = Depends(JWTBearer())):
    db_item = Manage(name=user.name)
    db.add(db_item)
    db.commit()@router.post('')
    return db_item


@router.put('{/User_id}')
def update(user_id: int, user: Users, db: Session = Depends(get_db)):
    old = db.query(Frame).filter(Manage.id == item_id).first()
    if old is None:
        raise HTTPException(status_code=404, detail='Item not found')
    id.name = user.name
    db.commit()
    return id


@router.delete('{/User_id}')
def delete(usere_id: int, user: Users, db: Session = Depends(get_db)):
    user = db.query(Manage).filter(Manage.id == user_id).first()
    db.delete(user)
    db.commit()
    return user
