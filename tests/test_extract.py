import pytest

from requests import Response, ConnectionError

from crossETL.extract import ApiExtractor

@pytest.fixture
def extractor():
    return ApiExtractor()

@pytest.fixture
def mock_response_error():
    def mock_json():
        return {'error': []}
    mock_response = Response()
    mock_response.json = mock_json
    return mock_response


def test_get_next_page_success(mocker, extractor):
    def mock_json():
        return {'numbers': [1,2,3]}
    def mock_get_success(link):
        response = Response()
        response.status_code = 200
        response.json = mock_json
        return response
    mocker.patch(
        'crossETL.extract.requests.get',
        mock_get_success
    )
    response = extractor.get_next_page()
    assert response.status_code == 200

def test_get_next_page_fail(mocker, extractor):
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
    response = extractor.get_next_page()
    assert response is None
    assert extractor.tries == 3

def test_error_in_response_true(mocker, extractor):
    def mock_json_error(self):
        return {'error': []}
    mocker.patch(
        'crossETL.extract.requests.Response.json',
        mock_json_error
    )
    mock_response = Response()
    error_in_response = extractor.error_in_response(mock_response)
    assert error_in_response is True

def test_error_in_response_false(mocker, extractor):
    def mock_json_numbers(self):
        return {'numbers': [1,2,3]}
    mocker.patch(
        'crossETL.extract.requests.Response.json',
        mock_json_numbers
    )
    mock_response = Response()
    error_in_response = extractor.error_in_response(mock_response)
    assert error_in_response is False    

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
    def mock_get_next_page(self):
        response = Response()
        response.status_code = 0
        if self.page <= 3:
            response.mock_json = {'numbers': [self.page]}
            self.page += 1
        else:
            response.mock_json = {'numbers': []}
        return response
    mocker.patch(
        'crossETL.extract.requests.Response.json',
        mock_json
    )
    mocker.patch(
        'crossETL.extract.ApiExtractor.get_next_page',
        mock_get_next_page
    )
    output = extractor.extract_api()
    assert extractor.page == 4
    assert output == [1,2,3]