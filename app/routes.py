from fastapi import APIRouter, HTTPException, Depends
from app.schemas import TaskCreate, TaskInDB, TaskUpdate
from app import crud
from app.dependencies import get_current_user 

router = APIRouter()
#multicuenta/multisession routes 

# Solo usuarios autenticados pueden crear tareas
@router.post("/tasks", response_model=TaskInDB)
async def create(task: TaskCreate, user=Depends(get_current_user)):
    return await crud.create_task(task, user["id"])

# Solo usuarios autenticados pueden ver las tareas
@router.get("/tasks", response_model=list[TaskInDB])
async def get_all(user=Depends(get_current_user)):
    return await crud.get_tasks(user["id"])

# Solo usuarios autenticados pueden actualizar tareas
@router.put("/tasks/{task_id}", response_model=TaskInDB)
async def update(task_id: str, update: TaskUpdate, user=Depends(get_current_user)):
    updated = await crud.update_task(task_id, update, user["id"])  # << aquí
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found or not authorized")
    return updated

# Solo usuarios autenticados pueden eliminar tareas
@router.delete("/tasks/{task_id}")
async def delete(task_id: str, user=Depends(get_current_user)):
    deleted = await crud.delete_task(task_id, user["id"])  # << aquí
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found or not authorized")
    return {"message": "Task deleted"}
