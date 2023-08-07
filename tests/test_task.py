import httpx
import pytest

from sqlalchemy.orm import Session

from database.database import get_database_session
from database.task import crud

from database import models

# @pytest.mark.asyncio
# async def test_create_task(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         'name': 'Tasks 1',
#         'description': 'Description Task',
#         'status': 'done',
#         'user_id': '1',
#         'category_id': '1',
#     }

#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }

#     response = await default_client.post('/tasks/', json=payload, headers=headers)
#     assert response.status_code == 201
#     assert response.json()['tasks']['name'] == payload['name']

# @pytest.mark.asyncio
# async def test_create_task_form(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         'name': 'Tasks 1',
#         'description': 'Description Task',
#         'status': 'done',
#         'user_id': '1',
#         'category_id': '1',
#     }

#     headers = {
#         'accept': 'application/json',
#         # 'Content-Type': 'application/json'
#     }

#     response = await default_client.post('/tasks/form-create', data=payload, headers=headers)

#     assert response.status_code == 201
#     assert response.json()['tasks']['name'] == payload['name']
    
# @pytest.mark.asyncio
# async def test_update_task(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         'id': '1',
#         'name': 'Tasks 2',
#         'description': 'Description Task',
#         'status': 'pending',
#         'user_id': '1',
#         'category_id': '1',
#     }

#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }

#     response = await default_client.put('/tasks/'+payload['id'], json=payload, headers=headers)

#     assert response.status_code == 200
#     assert response.json()['task']['name'] == payload['name']


# @pytest.mark.asyncio
# async def test_all_tasks(default_client: httpx.AsyncClient, db: Session = next(get_database_session())) -> None:

#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }

#     tasks = crud.getAll(db)
#     response = await default_client.get('/tasks/', headers=headers)

#     assert response.status_code == 200
#     assert len(tasks) == len(response.json()['tasks'])

@pytest.mark.asyncio
async def test_by_id_task(default_client: httpx.AsyncClient, db: Session = next(get_database_session())) -> None:

    id = 1

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    task = crud.getById(id,db)
    response = await default_client.get('/tasks/'+str(id), headers=headers)

    assert response.status_code == 200
    assert id == response.json()['id']
    assert task.name == response.json()['name']

@pytest.mark.asyncio
async def test_delete_task(default_client: httpx.AsyncClient, db: Session = next(get_database_session())) -> None:

    id = 2

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    } 

    response = await default_client.delete('/tasks/'+str(id), headers=headers)

    task = db.query(models.Task).get(id)
    # task = crud.getById(id)

    assert response.status_code == 200
    assert task is None
    assert "ok" == response.json()['msj']

@pytest.mark.asyncio
async def test_delete_task_not_exist(default_client: httpx.AsyncClient, db: Session = next(get_database_session())) -> None:

    id = 2

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    } 
    
    response = await default_client.delete('/tasks/'+str(id), headers=headers)

    task = db.query(models.Task).get(id)
    # task = crud.getById(id)

    assert response.status_code == 404
    assert task is None
