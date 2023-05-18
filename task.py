from fastapi import APIRouter, Body, status, HTTPException

from models import Task, StatusType

task_router = APIRouter()
task_list= [
]

@task_router.get("/",status_code=status.HTTP_200_OK)
def get():
    return { "tasks": task_list }

@task_router.post("/",status_code=status.HTTP_201_CREATED)
def add(task: Task = Body(
    examples={
        "normal1":{
            "summary":"A normal example 1",
            "description":"A normal example",
            "value":{
                "id" : 123,
                "name": "Salvar al mundo",
                "description": "Hola Mundo Desc",
                "status": StatusType.PENDING,
                "tag":["tag 1", "tag 2"],
                "category": {
                    "id":1234,
                    "name":"Cate 1"
                },
                "user": {
                    "id":12,
                    "name":"Andres",
                    "email":"admin@admin.com",
                    "surname":"Cruz",
                    "website":"http://desarrollolibre.net",
                }
            }
        },
        "normal2":{
            "summary":"A normal example 2",
            "description":"A normal example",
            "value":{
                "id" : 12,
                "name": "Sacar la basura",
                "description": "Hola Mundo Desc",
                "status": StatusType.PENDING,
                "tag":["tag 1"],
                "category": {
                    "id":1,
                    "name":"Cate 1"
                },
                "user": {
                    "id":12,
                    "name":"Andres",
                    "email":"admin@admin.com",
                    "surname":"Cruz",
                    "website":"http://desarrollolibre.net",
                }
            }
        },
        "invalid":{
            "summary":"A invalid example 1",
            "description":"A invalid example",
            "value":{
                "id" : 12,
                "name": "Sacar la basura",
                "description": "Hola Mundo Desc",
                "status": StatusType.PENDING,
                "tag":["tag 1"],
                "user": {
                    "id":12,
                    "name":"Andres",
                    "email":"admin@admin.com",
                    "surname":"Cruz",
                    "website":"http://desarrollolibre.net",
                }
            }
        }
    }
)):

    #verifica que el indice exista
    if task in task_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Task '+ task.name+' already exist')

    task_list.append(task)
    return { "tasks": task_list }

@task_router.put("/",status_code=status.HTTP_200_OK)
def update(index: int, task: Task = Body(
     example= {
                "id" : 123,
                "name": "Salvar al mundo 2",
                "description": "Hola Mundo Desc",
                "status": StatusType.PENDING,
                "tag":["tag 1", "tag 2"],
                "category": {
                    "id":1234,
                    "name":"Cate 1"
                },
                "user": {
                    "id":12,
                    "name":"Andres",
                    "email":"admin@admin.com",
                    "surname":"Cruz",
                    "website":"http://desarrollolibre.net",
                }
            }
)):
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

