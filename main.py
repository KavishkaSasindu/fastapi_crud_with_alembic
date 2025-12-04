from fastapi import FastAPI
from app.routers.person_router import router as person_router
from app.routers.item_router import router as item_router
app = FastAPI(title="My API", version="1.0.0")

app.include_router(person_router)
app.include_router(item_router)
@app.get("/")
def welcome():
    return {"message": "Welcome to My API!"}