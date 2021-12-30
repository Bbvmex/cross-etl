from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
app.config['DEBUG'] = True
app.data = []

# Using a Mock DB (.csv)
@app.route('/api/load/', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return jsonify(app.data)

    if request.method == 'POST':
        app.data = request.json
        return jsonify({'msg': 'Data added'})

def start_app():
    app.run()

if __name__ == '__main__':
    start_app()
