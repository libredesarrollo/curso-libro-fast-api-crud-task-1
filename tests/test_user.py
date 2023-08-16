from fastapi.testclient import TestClient

from database.database import get_database_session
from api import app

client = TestClient(app)
app.dependency_overrides[get_database_session] = get_database_session

def test_sign_new_user() -> None:

    payload = {
        'email': 'admintesttestclient@admin.com',
        'name': 'andres',
        'surname': 'cruz',
        'website': 'https://desarrollolibre.net/',
        'password': '12345'
    }

    response = client.post('/register', json=payload)

    assert response.status_code == 201
    assert response.json() == {
        "message": "User created succefully"
    }

    # assert response.status_code == 201
    # data = response.json()
    # assert data["email"] == "admintesttestclient@admin.com"
    # assert "id" in data

def test_login_user() -> None:

    payload = {
        'username': 'admintesttestclient@admin.com',
        'password': '12345'
    }
    
    response = client.post('/token', data=payload)

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_logout() -> None:
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Token': 'KAhfwSLxjYzclVKW13uJsut6-UC4w0XBPRXBnUWFMUg'
    }

    response = client.delete('/logout', headers=headers)

    assert response.status_code == 200
    assert response.json()['msj'] == 'ok'
