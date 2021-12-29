from flask import Flask, jsonify
import csv

app = Flask(__name__)
app.config['DEBUG'] = True

# Using a Mock DB (.csv)
@app.route('/api/load/', methods=['GET'])
def return_data():
    data = []
    with open('crossETL/data_sorted.csv', 'r') as inFile:
        reader = csv.reader(inFile)
        for row in reader:
            data = [float(i) for i in row]
            break
    return jsonify(data)

def start_app():
    app.run()

if __name__ == '__main__':
    start_app()
    # In another window
    # teste = requests.get('http://127.0.0.1:5000/api/load/')
    # print(len(teste.json()))