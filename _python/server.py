
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]




# app.py

from flask import Flask, jsonify, request



# jsonify to return python dicts to json 


app = Flask(__name__)

# Sample data

@app.route('/')
def home():
    return "Welcome to the API!"



@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)



# GET 
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201


# PUT 
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


# DELETE
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)









