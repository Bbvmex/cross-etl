import pytest

from requests import Response, ConnectionError

from crossETL.extract import ApiExtractor

@pytest.fixture
def extractor():
    return ApiExtractor()

def test_get_page_success(mocker, extractor):
    def mock_get_success(link):
        response = Response()
        response.status_code = 200
        return response
    mocker.patch(
        'crossETL.extract.requests.get',
        mock_get_success
    )
    response = extractor.get_page()
    assert response.status_code == 200

def test_get_page_fail(mocker, extractor):
    def mock_get_fail(link):
        response = Response()
        response.status_code = 500
        return response
    def mock_handle_error(self):
        self.tries += 1

    mocker.patch(
        'crossETL.extract.requests.get',
        mock_get_fail
    )
    mocker.patch(
        'crossETL.extract.ApiExtractor.handle_get_error',
        mock_handle_error
    )
    response = extractor.get_page()
    assert response is None
    assert extractor.tries == 3

def test_handle_get_error(extractor):
    extractor.response = Response()
    extractor.response.status_code = 0
    extractor.tries = 1
    extractor.handle_get_error()
    assert extractor.tries == 2
    with pytest.raises(ConnectionError):
        extractor.handle_get_error()

def test_extract_api(mocker, extractor):
    def mock_json(self):
        return self.mock_json
    def mock_get_page(self):
        response = Response()
        response.status_code = 0
        if self.page == 1:
            response.mock_json = {'numbers': [1, 2, 3]}
        elif self.page == 2:
            response.mock_json = {'error': ''}
            self.page += 1
        else:
            response.mock_json = {'numbers': []}
        return response

    mocker.patch(
        'crossETL.extract.requests.Response.json',
        mock_json
    )
    mocker.patch(
        'crossETL.extract.ApiExtractor.get_page',
        mock_get_page
    )
    output = extractor.extract_api()
    assert extractor.page == 3
    assert output == [1,2,3]