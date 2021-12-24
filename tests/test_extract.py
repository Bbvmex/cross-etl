import pytest

from crossETL.extract import api_extractor

@pytest.fixture
def extractor():
    return api_extractor()

def test_get_page(extractor):
    response = extractor.get_page()
    assert response.status_code == 200



