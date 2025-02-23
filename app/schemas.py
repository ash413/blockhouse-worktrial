from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .models import OrderType

class OrderCreate(BaseModel):
    symbol: str = Field(..., description="Trading symbol (e.g., BTC-USD)")
    quantity: float = Field(..., gt=0, description="Quantity to trade")
    price: float = Field(..., gt=0, description="Price per unit")
    order_type: OrderType = Field(..., description="Type of order (BUY/SELL)")

class OrderResponse(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True