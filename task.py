from fastapi import APIRouter, Body

from models import Task

task_router = APIRouter()
task_list= [
]

@task_router.get("/")
def get():
    return { "tasks": task_list }

@task_router.post("/")
def add(task: Task):
    task_list.append(task)
    return { "tasks": task_list }

@task_router.put("/")
def update(index: int, task: Task):
    # task_list[index] = {
    #     "task" : task.name,
    #     "status" : task.status,
    #     "description" : task.description,
    # }
    task_list[index] = task
    return { "tasks": task_list }

@task_router.delete("/")
def delete(index: int):
    del task_list[index] 
    return { "tasks": task_list }