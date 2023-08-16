import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from database.task import crud
from database import models
from api import app
from database.database import get_database_session

from authentication import authentication

client = TestClient(app)
app.dependency_overrides[get_database_session] = get_database_session

@pytest.fixture(scope='module')
def access_token(db : Session = next(get_database_session())) -> str:
    user = authentication.authenticate('admin@admin.com','12345',db)
    return authentication.create_access_token(user, db).access_token

def test_protected_fixed_route(access_token: str) -> None:
    
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Token': access_token
    }

    response = client.get("/protected-route", headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "hello" in data

def test_protect_route(access_token: str) -> None:

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {access_token}"
    }

    response = client.get('/hello',headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "hello" in data


