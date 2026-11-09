from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


items = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": True},
]


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(task: TaskCreate):
    new_item = {
        "id": len(items) + 1,
        "title": task.title,
        "completed": task.completed,
    }
    items.append(new_item)
    return new_item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"detail": "Item not found"}
