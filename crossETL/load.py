from flask import Flask, Blueprint
from flask import request, jsonify
import json

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['DEBUG'] = True
    #TODO ADD A DB -> Using a Json for now

    @app.route('/api/load', methods=['GET', 'POST'])
    def data():
        # TODO call extract and return the sorted data
        if request.method == 'GET':
            with open('crossETL/data.json', 'r') as inFile:
                data = json.load(inFile)
            return jsonify(data)

        if request.method == 'POST':
            with open('crossETL/data.json', 'w') as outFile:
                json.dump(request.json, outFile)
            return jsonify({'msg': 'Data added'})
    return app

def start_app() -> None:
    app = create_app()
    app.run()

if __name__ == '__main__':
    start_app()
