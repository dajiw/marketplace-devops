import os
import logging
from fastapi import FastAPI

# Настройка JSON-подобного логирования для будущей сборки в Loki
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Catalog Service")

PORT = int(os.getenv("PORT", 8001))

@app.get("/healthz")
def health_check():
    """Эндпоинт для проверки здоровья сервиса (Kubernetes Liveness/Readiness)"""
    return {"status": "ok", "service": "catalog-service"}

@app.get("/api/v1/products")
def get_products():
    logging.info("Fetching products catalog")
    return [
        {"id": 1, "name": "DevOps Handbook", "price": 45},
        {"id": 2, "name": "Kubernetes in Action", "price": 50},
        {"id": 3, "name": "Terraform Up & Running", "price": 40},
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)