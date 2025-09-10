from fastapi.testclient import TestClient
from guests_main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_add_and_list_guests():
    # começa vazio
    response = client.get("/guests")
    assert response.status_code == 200
    assert response.json() == []

    # adiciona um convidado
    response = client.post("/guests", json={"name": "ConvidadoTeste"})
    assert response.status_code == 201
    guest = response.json()
    assert guest["id"] == 1
    assert guest["name"] == "ConvidadoTeste"

    # lista agora deve ter 1
    response = client.get("/guests")
    guests = response.json()
    assert len(guests) == 1
    assert guests[0]["name"] == "ConvidadoTeste"
