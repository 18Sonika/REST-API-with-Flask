from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# ------------------ ROUTES ------------------------

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"message": "User not found"}), 404

# POST = Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data["id"]

    if user_id in users:
        return jsonify({"message": "User already exists"}), 400

    users[user_id] = {
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify({"message": "User added successfully"}), 201


# PUT = Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify({"message": "User updated successfully"}), 200


# DELETE = Remove user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
