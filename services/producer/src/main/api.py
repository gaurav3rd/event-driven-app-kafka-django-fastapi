from src.main import producer_app


@producer_app.get("/")
async def root():
    return {"message": "Hello World"}
