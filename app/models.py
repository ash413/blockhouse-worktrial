from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from .database import Base
import enum

class OrderType(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    quantity = Column(Float)
    price = Column(Float)
    order_type = Column(Enum(OrderType))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
