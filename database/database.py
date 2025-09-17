from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3306/fastapi"
# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi"
# DATABASE_URL = "mysql+pymysql://root@localhost:3306/fastapi"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Archivo SQLite en la raíz del proyecto
DATABASE_URL = "sqlite:///./app.db"

# SQLite necesita este argumento para evitar errores de threading
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database_session():
    try:
        db = SessionLocal()
        yield db
        #return db
    finally:
        db.close()