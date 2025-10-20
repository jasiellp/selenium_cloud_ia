from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import item_schema
from app.services import item_service

router = APIRouter(prefix="/items", tags=["Itens"])

@router.post("/", response_model=item_schema.ItemResponse)
def criar_item(item: item_schema.ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)

@router.get("/", response_model=list[item_schema.ItemResponse])
def listar_itens(db: Session = Depends(get_db)):
    return item_service.get_items(db)
