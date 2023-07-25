import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:

    payload = {
        'email': 'admintest@admin.com',
        'name': 'andres',
        'surname': 'cruz',
        'website': 'https://desarrollolibre.net/',
        'password': '12345'
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = await default_client.post('/register', json=payload, headers=headers)

    assert response.status_code == 201
    assert response.json() == {
        "message": "User created succefully"
    }


