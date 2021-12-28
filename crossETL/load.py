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


@app.route('/', methods=['GET'])
def hello_world():
    return 'hello world'

if __name__ == '__main__':

    app.run()