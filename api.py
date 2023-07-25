from authentication.authentication import verify_access_token
from database.models import Task, Category, User, AccessToken
from database.task import crud
from database.database import Base, engine, get_database_session
from myupload import upload_router
from user import user_router
from task import task_router
from fastapi import FastAPI, Depends, APIRouter, Query, Path, Request, Header, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.templating import Jinja2Templates

import time
from typing import Optional
from typing_extensions import Annotated

from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="templates/")


app = FastAPI()
router = APIRouter()

Base.metadata.create_all(bind=engine)

# middlewares
# @app.middleware("http")
# async def add_process_time_to_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print("process_time")
#     print(process_time)
#     return response
# middlewares

# TOKENS AUTH

# TOKEN SIN BD
# API_KEY_TOKEN = "SECRET_PASSWORD"
# api_key_token = APIKeyHeader(name='Token')
# @app.get("/protected-route")
# def protected_route(token: str = Depends(api_key_token)):
#     if token != API_KEY_TOKEN:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return { 'hello':'fastapi' }
# TOKEN CON BD esquema inicial
# api_key_token = APIKeyHeader(name='Token')
# def protected_route(token: str = Depends(api_key_token), db: Session = Depends(get_database_session)):
#     user = db.query(User).join(AccessToken).filter(AccessToken.access_token == token).first()
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
# return { 'hello':'fastapi' }
# TOKENS AUTH

# @router.get('/hello', dependencies=[Depends(verify_access_token)])


@router.get('/hello')
def hello_world(user=Depends(verify_access_token), db: Session = Depends(get_database_session)):
    print("********")
    print(user.name)
    return {"hello": "world"}


@app.get("/e_page")
def page(page: int = Query(1, ge=1, le=20, title='Esta es la pagina que quieres ver'), size: int = Query(5, ge=5, le=20, title='Cuantos registros por pagina')):
    return {"page": page, "size": size}


@app.get("/e_phone/")  # +34 111 12-34-56
# def phone(phone: str = Query(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", example="+34 111 12-34-56")):
def phone(phone: Annotated[str, Query(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", example="+34 111 12-34-56")]):
    return {"phone": phone}


@app.get("/ep_phone/{phone}")  # +34 111 12-34-56
# def phone(phone: str = Path(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", examples={
#     "normal": {
#         "summary": "A normal example",
#         "description": "A normal example",
#         "value":
#             "+34 111 12-34-56"
#     },
#     "normal 2": {
#         "summary": "A normal example 2",
#         "description": "A normal example",
#         "value":
#             "+34 123 12-34-58"

#     }
# })
def phone(phone: Annotated[str, Path(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", examples={
    "normal": {
        "summary": "A normal example",
        "description": "A normal example",
        "value":
            "+34 111 12-34-56"
    },
    "normal 2": {
        "summary": "A normal example 2",
        "description": "A normal example",
        "value":
            "+34 123 12-34-58"

    }
})]
):
    return {"phone": phone}


# templaples
@app.get('/page')
def index(request: Request, db: Session = Depends(get_database_session)):
    categories = db.query(Category).all()
    return templates.TemplateResponse('task/index.html', {"request": request, 'tasks': crud.getAll(db), 'categories': categories})


# DEPENDS
def pagination(page: Optional[int] = 1, limit: Optional[int] = 10):
    return {'page': page-1, 'limit': limit}


@app.get('/p-task')
def index(pag: dict = Depends(pagination)) -> dict:
    # print(pag.get('page'))
    return pag

# PATH


def validate_token(token: str = Header()) -> None:
    if token != "TOKEN":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

# @app.get('/route-protected', dependencies=[Depends(validate_token)])
# def protected_route(index:int):
#     return {'hello': 'FastAPI'}


# VAR
CurrentTaskId = Annotated[int, Depends(validate_token)]
@app.get('/route-protected2')
def protected_route2(CurrentTaskId, index: int) -> dict:
    return {'hello': 'FastAPI'}

# DEPENDS


app.include_router(router)
app.include_router(task_router, prefix='/tasks')
app.include_router(user_router)
app.include_router(upload_router, prefix='/upload')
