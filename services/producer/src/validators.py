from pydantic import BaseModel, constr


class AddTodoModel(BaseModel):
    title: constr(min_length=1, max_length=50)
    description: constr(min_length=1, max_length=100)
