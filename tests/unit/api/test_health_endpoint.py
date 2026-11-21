from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from llm_reply_reviewer.api.main import app


@pytest.fixture
def client() -> Generator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client


def test_health_endpoint_returns_healthy(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
