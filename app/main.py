from fastapi import FastAPI, Depends, WebSocket, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

app = FastAPI(
    title="Trading API",
    description="A simple trading api for handling orders",
    version="1.0.0"
)

# create tables on startup
models.Base.metadata.create_all(bind=database.engine)

@app.post("/orders/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders/", response_model=List[schemas.OrderResponse])
def list_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    orders = db.query(models.Order).offset(skip).limit(limit).all()
    return orders



#   BONUS - WEBSOCKET 
@app.websocket("/ws")
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"New Order Created! {data}")