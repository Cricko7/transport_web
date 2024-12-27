import os
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

stations = []

@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.get_json()
    stations.append(data)
    return jsonify({"message": "Станция добавлена", "stations": stations}), 201

if __name__ == '__main__':
    app.run(debug=True)
