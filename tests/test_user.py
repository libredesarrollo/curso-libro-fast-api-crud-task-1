import httpx
import pytest


# @pytest.mark.asyncio
# async def test_create_token(default_client: httpx.AsyncClient) -> None:
#     payload = {
#         'username': 'admin@admin.com',
#         'password': '12345'
#     }

#     headers = {
#         'accept': 'application/json',
#         # 'Content-Type': 'application/json'
#     }

#     response = await default_client.post('/token', data=payload, headers=headers)

#     assert response.status_code == 200
#     assert "access_token" in response.json()

# @pytest.mark.asyncio
# async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:

#     payload = {
#         'email': 'admintest@admin.com',
#         'name': 'andres',
#         'surname': 'cruz',
#         'website': 'https://desarrollolibre.net/',
#         'password': '12345'
#     }

#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }

#     response = await default_client.post('/register', json=payload, headers=headers)

#     assert response.status_code == 201
#     assert response.json() == {
#         "message": "User created succefully"
#     }


@pytest.mark.asyncio
async def test_logout(default_client: httpx.AsyncClient) -> None:
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Token': 'lYDVdzjgn3sVf-tpkxqfYMikld0yvQRah_YZo9bvF6M'
    }

    response = await default_client.delete('/logout', headers=headers)

    assert response.status_code == 200
    assert response.json()['msj'] == 'ok'
