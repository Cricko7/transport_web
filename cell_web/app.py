import os
import sqlite3
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('stations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frequency TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.before_first_request
def initialize():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

stations = []

@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.get_json()
    try:
        # Здесь можно добавить проверку данных
        stations.append(data)  # В дальнейшем замените на запись в БД
        return jsonify({"message": "Станция добавлена", "stations": stations}), 201
    except Exception as e:
        return jsonify({"message": "Ошибка при добавлении станции", "error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
