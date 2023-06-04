from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, validator, Field, EmailStr, HttpUrl

class StatusType(str,Enum):
    DONE = "done"
    PENDING = "pending"

class MyBaseModel(BaseModel):
    pass
    # id:int = Field(gt=1, le=10000)

    # @validator('id')
    # def id_greater_than_zero(cls, v):
    #     if v<=0 :
    #         raise ValueError('must be greater than zero')
    #     return v
    
    # @validator('id')
    # def id_less_than_thousand(cls, v):
    #     if v >= 10000 :
    #         raise ValueError('must be less than thousand')
    #     return v

class Category(MyBaseModel):
    name: str
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id" : 1234,
    #             "name": "Cate 1"
    #         }
    #     }

class User(MyBaseModel):
    name: str = Field(min_length=5)
    surname: str
    email: EmailStr
    website: str #HttpUrl

class Task(MyBaseModel):
    name: str
    description: Optional[str] = Field("No description",min_length=5)
    status: StatusType
    # category: Category
    # user: User
    # tags: List[str] = []

    
    category_id: int = Field(gt=0)
    user_id: int = Field(gt=0)
    # tags: set[str] = set()

    class Config:
        orm_mode=True
        schema_extra = {
            "example": {
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
        }

    @validator('name')
    def name_alphanumeric_and_whitespace(cls, v):
        if v.replace(" ", '').isalnum():
            return v
        raise ValueError('must be a alphanumeric')
        


