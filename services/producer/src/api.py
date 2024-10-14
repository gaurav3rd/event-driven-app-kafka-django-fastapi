from .main import producer_app
from .validators import AddTodoModel
from src.config import send_to_topic

# from config import send_to_topic


@producer_app.post("/new/")
async def create(item: AddTodoModel):
    if send_to_topic("todo-create", item.dict()):
        return {"message": "Todo added successfully"}
    return {"message": "Could not create new todo item"}
