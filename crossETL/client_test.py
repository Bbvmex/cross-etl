import requests

from extract import ApiExtractor
from transform import quicksort

if __name__ == '__main__':
    # Run load.py first to start the Flask app
    extractor = ApiExtractor()
    data = extractor.extract_api()
    sorted = quicksort(data)
    save = requests.post('http://127.0.0.1:5000/api/load/', json=sorted)
    load = requests.get('http://127.0.0.1:5000/api/load/')
    print(len(load.json()))
