from sqlalchemy.orm import Session

from database.pagination import paginate, PageParams
from database import models
from schemes import Task

def getAll(db: Session):
    tasks = db.query(models.Task).all()
    return tasks

def getById(id: int, db: Session):
    # task = db.query(models.Task).filter(models.Task.id == id).first()
    task = db.query(models.Task).get(id)
    return task

def create(task: Task, db: Session):
    taskdb = models.Task(name=task.name, description=task.description, status=task.status, category_id = task.category_id, user_id = task.user_id)
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

def update(id: int, task: Task, db: Session):
    
    taskdb = getById(id, db)
    
    taskdb.name = task.name
    taskdb.description = task.description
    taskdb.status = task.status
    taskdb.category_id = task.category_id

    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

def delete(id: int, db: Session):
    
    taskdb = getById(id, db)

    db.delete(taskdb)
    db.commit()


def pagination(page: int, size:int, db: Session):
    pageParams = PageParams()
    # pageParams.page = page
    # pageParams.size = size
    return paginate(pageParams, db.query(models.Task), Task)