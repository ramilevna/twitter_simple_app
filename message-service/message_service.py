from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# In-memory message storage (use a database for production)
messages = []


# Route to post a new message (only for registered users)
@app.route('/messages', methods=['POST'])
def post_message():
    data = request.json
    username = data.get('username')
    content = data.get('content')
    
    # Validate input
    if not username or not content:
        return jsonify({'error': 'Username and content are required'}), 400
    if len(content) > 400:
        return jsonify({'error': 'Message exceeds 400 characters'}), 400
    
    # Check if user is registered by calling User Service
    user_check = requests.get(f"http://user-service:5001/users/{username}")
    
    if user_check.status_code == 404:
        return jsonify({'error': 'User not registered'}), 403
    
    # Post the message
    message = {'username': username, 'content': content}
    messages.append(message)
    
    # Limit to last 10 messages (FIFO)
    if len(messages) > 10:
        messages.pop(0)
    
    return jsonify({'message': 'Message posted successfully'}), 201

# Route to get the last 10 messages (public feed)
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)


