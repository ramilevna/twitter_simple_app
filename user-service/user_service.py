from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (use a database for production)
users = {}

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    
    # Validate input
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    if username in users:
        return jsonify({'error': 'Username already exists'}), 409
    
    # Register user
    users[username] = {'username': username}
    return jsonify({'message': f'User {username} registered successfully'}), 201

# Route to check if a user is registered
@app.route('/users/<username>', methods=['GET'])
def check_user(username):
    if username in users:
        return jsonify({'username': username, 'status': 'registered'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)


