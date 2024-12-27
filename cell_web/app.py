from flask import Flask, request, jsonify

app = Flask(__name__)

stations = []

@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.get_json()
    stations.append(data)
    return jsonify({"message": "Станция добавлена", "stations": stations}), 201

if __name__ == '__main__':
    app.run(debug=True)
