
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Enum

from database.database import Base
from schemes import StatusType

class Task(Base):
    __tablename__ = "tasks"
    id=Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    description = Column(Text())
    status = Column(Enum(StatusType))
