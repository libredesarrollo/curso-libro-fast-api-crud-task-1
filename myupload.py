from fastapi import APIRouter, File, UploadFile

import shutil
from typing import List

upload_router = APIRouter()

@upload_router.post("/file")
def upload_file(file: bytes = File()):
    return { "file_size" : len(file) }

@upload_router.post("/uploadfile1")
def upload_uploadfile1(file: UploadFile):
    return { 
        "filename" : file.filename,
        "content_type" : file.content_type,
    }

@upload_router.post("/uploadfile2")
def upload_uploadfile2(file: UploadFile):

    with open("img/image.png","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return { 
        "filename" : file.filename
    }

@upload_router.post("/uploadfile3")
def upload_uploadfile3(images: List[UploadFile] = File()):

    for image in images:
        with open("img/"+image.filename,"wb") as buffer:
            shutil.copyfileobj(image.file, buffer)