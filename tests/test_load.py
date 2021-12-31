import pytest

import json

from crossETL.load import create_app

@pytest.fixture
def client():
    test_app = create_app()
    test_app.config['TESTING'] = True
    with test_app.test_client() as client:
        with test_app.app_context():
            yield client

def test_api_load_post(client):
    p = client.post('/api/load', json=json.dumps([1.5, 3.55, 4.2]))
    assert p.status_code == 200
    r = client.get('api/load')
    assert r.status_code == 200
    assert r.json == json.dumps([1.5, 3.55, 4.2])
