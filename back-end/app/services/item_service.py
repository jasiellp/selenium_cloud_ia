from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item_schema import ItemCreate


def create_item(db: Session, item: ItemCreate):
    db_item = Item(nome=item.nome, descricao=item.descricao)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session):
    return db.query(Item).all()
