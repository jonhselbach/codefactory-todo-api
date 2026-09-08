import os
import tempfile
import pytest

os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")

from app.main import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_create_and_list_task(client):
    response = client.post("/tasks", json={"title": "Estudar DevOps"})
    assert response.status_code == 201
    task_id = response.get_json()["id"]

    response = client.get("/tasks")
    assert response.status_code == 200
    titles = [task["title"] for task in response.get_json()]
    assert "Estudar DevOps" in titles

    response = client.put(f"/tasks/{task_id}", json={"done": True})
    assert response.status_code == 200
    assert response.get_json()["done"] is True

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204


def test_create_task_without_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_update_missing_task_returns_404(client):
    response = client.put("/tasks/9999", json={"done": True})
    assert response.status_code == 404
