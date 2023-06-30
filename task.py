from fastapi import APIRouter, Depends, Body, Path, status
from sqlalchemy.orm import Session

from database.database import get_database_session
from database.task import crud

from schemes import Task, TaskRead, TaskWrite
from dataexample import taskWithORM

task_router = APIRouter()

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
    # return { "tasks": [ TaskRead.from_orm(task) for task in crud.getAll(db) ] }

@task_router.get("/{id}",status_code=status.HTTP_200_OK)
def get(id: int = Path(ge=1), db: Session = Depends(get_database_session)):
    return crud.getById(id, db)
    # return Task.from_orm(crud.getById(id, db))
# def add(request: Request, task:TaskWrite = Depends(TaskWrite.as_form), db: Session = Depends(get_database_session)):
@task_router.post("/form-create",status_code=status.HTTP_201_CREATED)
def addForm(task: TaskWrite = Depends(TaskWrite.as_form), db: Session = Depends(get_database_session)):
    return { "tasks": crud.create(task,db=db) }

@task_router.post("/",status_code=status.HTTP_201_CREATED)
def add(task: TaskWrite = Body(
    examples=taskWithORM
), db: Session = Depends(get_database_session)):

    # return { "tasks": TaskWrite.from_orm(crud.create(task,db=db)) }
    return { "tasks": crud.create(task,db=db) }

@task_router.put("/{id}",status_code=status.HTTP_200_OK)
def update(id: int = Path(ge=1), task: TaskWrite = Body(
     examples=taskWithORM), db: Session = Depends(get_database_session)):

    return { "task": crud.update(id, task, db) }

@task_router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete(id: int = Path(ge=1), db: Session = Depends(get_database_session)):
    crud.delete(id,db)
    return { "tasks": crud.getAll(db) }

#******** tag
@task_router.put("/tag/add/{id}",status_code=status.HTTP_200_OK)
def tagAdd(id: int = Path(ge=1), idTag:int = Body(ge=1), db: Session = Depends(get_database_session)):
    return crud.tagAdd(id,idTag,db)

@task_router.delete("/tag/remove/{id}",status_code=status.HTTP_200_OK)
def tagRemove(id: int = Path(ge=1), idTag:int = Body(ge=1), db: Session = Depends(get_database_session)):
    return crud.tagRemove(id, idTag, db)
