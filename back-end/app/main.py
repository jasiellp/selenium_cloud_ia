from fastapi import FastAPI
from app.routes import item_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Template Example")

app.include_router(item_router.router)

@app.get("/")
def root():
    return {"message": "API está rodando 🚀"}
