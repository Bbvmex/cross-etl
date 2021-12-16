import requests

def extract_api():
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


if __name__ == '__main__':
    teste = extract_api()

    with open('data.txt', 'w') as f:
        for item in teste:
            f.write(f'{item}\n')
    
    