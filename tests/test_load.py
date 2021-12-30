import pytest

import json

from crossETL.load import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_load_post(client):
    r = client.post('/api/load/', json=json.load([1.5, 3.55, 4.2]))
    assert r == 200
    assert r.json() == [1.5, 3.55, 4.2]
    assert client.data == [1.5, 3.55, 4.2]
