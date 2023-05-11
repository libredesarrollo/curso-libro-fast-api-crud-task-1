from fastapi import APIRouter, Body, status, HTTPException

from models import Task

task_router = APIRouter()
task_list= [
]

@task_router.get("/",status_code=status.HTTP_200_OK)
def get():
    return { "tasks": task_list }

@task_router.post("/",status_code=status.HTTP_201_CREATED)
def add(task: Task):

    #verifica que el indice exista
    if task in task_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Task '+ task.name+' already exist')

    task_list.append(task)
    return { "tasks": task_list }

@task_router.put("/",status_code=status.HTTP_200_OK)
def update(index: int, task: Task):
    # task_list[index] = {
    #     "task" : task.name,
    #     "status" : task.status,
    #     "description" : task.description,
    # }

    #verifica que el indice exista
    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Task ID does not exist')

    task_list[index] = task
    return { "tasks": task_list }

@task_router.delete("/",status_code=status.HTTP_200_OK)
def delete(index: int):

    #verifica que el indice exista
    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Task ID does not exist')

    del task_list[index] 
    return { "tasks": task_list }