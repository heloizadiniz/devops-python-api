import pytest
from fastapi.testclient import TestClient

from app.main import app, tasks

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tasks() -> None:
    """Isola os testes, limpando o armazenamento em memória."""

    tasks.clear()


def test_health_returns_version() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "2.0.0"}


def test_list_starts_empty() -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_and_list_task() -> None:
    created = client.post("/tasks", json={"title": "Estudar GitHub Actions"})
    listed = client.get("/tasks")

    assert created.status_code == 201
    assert created.json() == {
        "id": 1,
        "title": "Estudar GitHub Actions",
        "done": False,
    }
    assert listed.json() == [created.json()]


def test_rejects_short_title() -> None:
    response = client.post("
