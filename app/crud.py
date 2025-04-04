from app.database import db
from app.schemas import TaskCreate, TaskUpdate
from bson import ObjectId

def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task.get("description"),
        "status": task["status"]
    }

async def create_task(task: TaskCreate, user_id: str):
    new_task = task.dict()
    new_task["user_id"] = user_id
    result = await db.tasks.insert_one(new_task)
    created = await db.tasks.find_one({"_id": result.inserted_id})
    return task_helper(created)

async def get_tasks(user_id: str):
    tasks = []
    async for task in db.tasks.find({"user_id": user_id}):
        tasks.append(task_helper(task))
    return tasks

async def update_task(task_id: str, update_data: TaskUpdate, user_id: str):
    update_fields = update_data.dict(exclude_unset=True)
    if not update_fields:
        return None

    result = await db.tasks.update_one(
        {"_id": ObjectId(task_id), "user_id": user_id},  # valida que le pertenezca al usuario
        {"$set": update_fields}
    )

    if result.modified_count:
        updated = await db.tasks.find_one({"_id": ObjectId(task_id)})
        return task_helper(updated)

async def delete_task(task_id: str, user_id: str):
    result = await db.tasks.delete_one({"_id": ObjectId(task_id), "user_id": user_id})
    return result.deleted_count > 0
