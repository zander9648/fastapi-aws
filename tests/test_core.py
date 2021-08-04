from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_main_resource():
    response_auth = client.get("/")
    assert response_auth.status_code == 200

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}