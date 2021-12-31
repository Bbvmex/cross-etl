import requests
from requests.models import Response

class ApiExtractor():
    '''Class for handling the API data
    Extracts data from all pages
    Stops when reading a []
    Returns single array with all the data'''
    def __init__(self):
        self.link = 'http://challenge.dienekes.com.br/api/numbers?page='
        self.page = 1
        self.output = []
        self.tries = 0

    @staticmethod
    def error_in_response(response) -> None:
        '''Handles custom errors returned by the consulted API'''
        if 'error' in response.json().keys():
            return True
        else:
            return False

    def get_next_page(self) -> Response:
        print(self.page)
        response = requests.get(f'{self.link}{self.page!s}')
        self.response = response
        if response.status_code == 200 and not error_in_response(response):
            self.page += 1
            self.tries = 0
            return response
        else:
            self.handle_get_error()
            if self.tries < 3:
                return self.get_next_page()

    def handle_get_error(self) -> None:
        '''Raise an exception after 3 unsuccessful tries
        Otherwise just prints the page with an error'''
        self.tries += 1
        print (f'Could not get page {self.page!s} - Code {self.response.status_code!s} - Try {self.tries!s} of 3')
        if self.tries == 3:
            raise requests.ConnectionError
    
    def extract_api(self) -> list:
        while response := self.get_next_page():
            data = response.json()
            if data['numbers'] == []:
                return self.output 
            else:
                self.output.extend(data['numbers'])
            
if __name__ == '__main__':
    import json
    extractor = ApiExtractor()
    data = extractor.extract_api()
    with open('crossETL/data.json', 'w') as outFile:
        json.dump(data, outFile)
    