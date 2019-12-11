
def test_register(client):
    response = client.post(
        '/api/v1/auth', data={'username': '111', 'password': '1111'}
        )
    print(response.data)
    
    assert response.status_code == 201