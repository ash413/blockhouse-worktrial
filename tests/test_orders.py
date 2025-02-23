import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

# fixture - create test client
@pytest.fixture
def client():
    # database tables
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # drop database tables after test
    Base.metadata.drop_all(bind=engine)

# TEST - creating an order
def test_create_order(client):
    response = client.post(
        "/orders/",
        json={
            "symbol": "BTC-USD",
            "quantity": 1.5,
            "price": 50000,
            "order_type": "BUY",
        },
    )
    assert response.status_code == 200
    assert response.json()["symbol"] == "BTC-USD"
    assert response.json()["quantity"] == 1.5
    assert response.json()["price"] == 50000
    assert response.json()["order_type"] == "BUY"



# TEST - listing orders
def test_list_orders(client):
    # create order first
    client.post(
        "/orders/",
        json={
            "symbol": "BTC-USD",
            "quantity": 1.5,
            "price": 50000,
            "order_type": "BUY",
        },
    )
    # list orders
    response = client.get("/orders/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["symbol"] == "BTC-USD"