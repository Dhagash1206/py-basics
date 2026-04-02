from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get('name')
    data.append(item)
    return jsonify({"message": "Added", "data": data})

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data[index] = request.json.get('name')
    return jsonify({"message": "Updated", "data": data})

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    data.pop(index)
    return jsonify({"message": "Deleted", "data": data})

if __name__ == '__main__':
    app.run(debug=True)