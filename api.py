from fastapi import FastAPI, Depends, APIRouter, Query, Path, Request, Header, HTTPException, status
from fastapi.templating import Jinja2Templates

from typing import Optional
from typing_extensions import Annotated

from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="templates/")

from task import task_router
from myupload import upload_router

from database.database import Base, engine, get_database_session
from database.task import crud
from database.models import Task, Category

app = FastAPI()
router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get('/hello')
def hello_world(db: Session = Depends(get_database_session)):
    return { "hello": "world" }

@app.get("/e_page")
def page(page: int = Query(1, ge=1, le=20, title='Esta es la pagina que quieres ver'), size: int = Query(5, ge=5, le=20, title='Cuantos registros por pagina')):
    return { "page": page,"size": size }

@app.get("/e_phone/") # +34 111 12-34-56
def phone(phone: str = Query(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", example="+34 111 12-34-56")):
    return {"phone": phone}

@app.get("/ep_phone/{phone}") # +34 111 12-34-56
def phone(phone: str = Path(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$" , examples={
    "normal": {
        "summary":"A normal example",
        "description":"A normal example",
        "value" :
            "+34 111 12-34-56"
    },
    "normal 2": {
        "summary":"A normal example 2",
        "description":"A normal example",
        "value" :
            "+34 123 12-34-58"
        
    }
})):
    return {"phone": phone}


#templaples
@app.get('/page')
def index(request: Request, db: Session = Depends(get_database_session)):
    categories = db.query(Category).all()
    return templates.TemplateResponse('task/index.html',{"request": request, 'tasks': crud.getAll(db), 'categories': categories})



#DEPENDS
def pagination(page:Optional[int] = 1, limit:Optional[int] = 10):
    return {'page':page-1, 'limit':limit}

@app.get('/p-task')
def index(pag:dict = Depends(pagination)):
    # print(pag.get('page'))
    return pag

#PATH
def validate_token(token: str = Header()):
    if token != "TOKEN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
@app.get('/route-protected', dependencies=[Depends(validate_token)])
def protected_route(index:int):
    return {'hello': 'FastAPI'}

#VAR
CurrentTaskId = Annotated[int, Depends(validate_token)]
@app.get('/route-protected2')
def protected_route2(CurrentTaskId,index:int):
    return {'hello': 'FastAPI'}
#DEPENDS

app.include_router(router)
app.include_router(task_router, prefix='/tasks')
app.include_router(upload_router, prefix='/upload')