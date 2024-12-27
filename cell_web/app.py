import os
import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Инициализация базы данных
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

# Обработка маршрута главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Обработка добавления станции
@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.get_json()
    try:
        # Сохранение станции в базу данных
        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO stations (frequency, location) VALUES (?, ?)', 
                       (data['frequency'], data['location']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Станция добавлена"}), 201
    except Exception as e:
        return jsonify({"message": "Ошибка при добавлении станции", "error": str(e)}), 400

if __name__ == '__main__':
    init_db()  # Инициализация базы данных при запуске приложения
    app.run(debug=True)
