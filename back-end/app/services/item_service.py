from sqlalchemy.orm import Session
from app import models, schemas

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.item.Item(nome=item.nome, descricao=item.descricao)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models.item.Item).all()
