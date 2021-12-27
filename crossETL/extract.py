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

    def get_page(self) -> Response:
        response = requests.get(self.link+str(self.page))
        if response.status_code == 200:
            self.response = response
            return response
        else:
            self.handle_get_error()
            if self.tries < 3:
                return self.get_page()

    def handle_get_error(self) -> None:
        '''Raise an exception after 3 unsuccessful tries
        Otherwise just prints the page with an error'''
        self.tries += 1
        print ('Could not get page {} - Code {} - Try {} of 3'.format(str(self.page),
                                                        str(self.response.status_code),
                                                        str(self.tries)
                                                        ))
        if self.tries == 3:
            raise requests.ConnectionError
    
    def extract_api(self) -> list:
        while response := self.get_page():
            # print(self.page)
            self.tries = 0
            data = response.json()
            if 'error' in data.keys():
                # Sometimes the returned data comes only with an error
                pass
            elif data['numbers'] == []:
                return self.output
            else:
                self.output.extend(data['numbers'])
                self.page += 1

'''
def extract_api():
    # Using requests, 
    link = 'http://challenge.dienekes.com.br/api/numbers?page='
    page = 1
    output = []
    tries = 0

    while True:
        data = requests.get(link+str(page))
        if data.status_code == 200:
            tries = 0
            data = data.json()
            try:
                if data['numbers'] == []:
                    return output
            except KeyError:
                if 'error' in data.keys():
                    pass
                else:
                    print ('Error getting page {}'.format(str(page)))
                    raise KeyError
            print (page)
            output.extend(data['numbers'])
            page += 1
        else:
            tries += 1
            print ('Could not get page {} - Code {} - Try {} of 3'.format(str(page),
                                                            str(data.status_code),
                                                            str(tries)
                                                            ))
            if tries == 3:
                raise requests.ConnectionError
            continue
'''

if __name__ == '__main__':
    # teste = extract_api()
    extractor = ApiExtractor()
    teste2 = extractor.extract_api()
    with open('data2.txt', 'w') as f:
        for item in teste2:
            f.write(f'{item}\n')
    
    