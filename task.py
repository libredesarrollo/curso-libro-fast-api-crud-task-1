from fastapi import APIRouter, Depends, Body, status, HTTPException
from sqlalchemy.orm import Session

from database.database import get_database_session
from database.task import crud
from database import models

from schemes import Task, StatusType
from dataexample import taskWithORM

task_router = APIRouter()
task_list= [
]
    
@task_router.get("/",status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_database_session)):
    # SELECT * FROM tasks WHERE id = 1
    # task = crud.getById(db=db,id=1)
    
    # print(task.user.website)
    # print(db.query(models.Category).get(2).tasks[0])    
    # print(db.query(models.User).get(1).tasks)    
    # print(crud.getAll(db=db)[1].name)
    # crud.create(Task(name='Test',description='Descr', status= StatusType.DONE, category_id=1, user_id=1),db=db)
    # crud.update(1,Task(name='HOla MUndo 2',description='Descr', status= StatusType.DONE, category_id=2, user_id=1),db=db)
    # print(crud.pagination(1,2,db))
    
    return { "tasks": crud.getAll(db) }

@task_router.post("/",status_code=status.HTTP_201_CREATED)
def add(task: Task = Body(
    examples=taskWithORM
), db: Session = Depends(get_database_session)):

    #verifica que el indice exista
    # if task in task_list:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail='Task '+ task.name+' already exist')

    crud.create(task,db=db)

    task_list.append(task)
    return { "tasks": task_list }

@task_router.put("/",status_code=status.HTTP_200_OK)
def update(id: int, task: Task = Body(
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
), db: Session = Depends(get_database_session)):
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
def delete(index: int, db: Session = Depends(get_database_session)):

    crud.delete(1,db)

    #verifica que el indice exista
    if len(task_list) <= index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Task ID does not exist')

    del task_list[index] 
    return { "tasks": task_list }

