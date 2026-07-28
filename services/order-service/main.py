import os
import logging
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Order Service")

PORT = int(os.getenv("PORT", 8002))

class Order(BaseModel):
    product_id: int
    quantity: int

@app.get("/healthz")
def health_check():
    return {"status": "ok", "service": "order-service"}

@app.post("/api/v1/orders")
def create_order(order: Order):
    logging.info(f"Creating order for product_id: {order.product_id}, qty: {order.quantity}")
    return {
        "status": "created",
        "order_id": 101,
        "product_id": order.product_id,
        "quantity": order.quantity
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)