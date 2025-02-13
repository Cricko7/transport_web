import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Инициализация БД
def init_db():
    conn = sqlite3.connect('stations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frequency TEXT NOT NULL,
            location TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.get_json()
    try:
        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO stations (frequency, location, latitude, longitude) VALUES (?, ?, ?, ?)', 
                       (data['frequency'], data['location'], data['latitude'], data['longitude']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Станция добавлена"}), 201
    except Exception as e:
        return jsonify({"message": "Ошибка при добавлении станции", "error": str(e)}), 400

@app.route('/stations', methods=['GET'])
def get_stations():
    conn = sqlite3.connect('stations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, frequency, location, latitude, longitude FROM stations')
    stations = cursor.fetchall()
    conn.close()
    return jsonify(stations)

@app.route('/delete_station/<int:id>', methods=['DELETE'])
def delete_station(id):
    try:
        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM stations WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Станция удалена"}), 200
    except Exception as e:
        return jsonify({"message": "Ошибка при удалении станции", "error": str(e)}), 400

@app.route('/edit_station/<int:id>', methods=['PUT'])
def edit_station(id):
    data = request.get_json()
    try:
        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE stations SET frequency=?, location=?, latitude=?, longitude=? WHERE id=?', 
                       (data['frequency'], data['location'], data['latitude'], data['longitude'], id))
        conn.commit()
        conn.close()
        return jsonify({"message": "Станция обновлена"}), 200
    except Exception as e:
        return jsonify({"message": "Ошибка при обновлении станции", "error": str(e)}), 400

if __name__ == '__main__':
    init_db()  # Инициализация базы данных при запуске приложения
    app.run(debug=True)
