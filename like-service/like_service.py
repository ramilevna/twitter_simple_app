from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In-memory likes storage (use a database for production)
likes = {}

# Configuration
MESSAGE_SERVICE_URL = "http://message-service:5002"  # URL of the Message Service

# Route to like a message
@app.route('/likes/<int:message_id>', methods=['POST'])
def like_message(message_id):
    # Check if the message exists by calling the Message Service
    message_check = requests.get(f"{MESSAGE_SERVICE_URL}/messages")
    
    if message_check.status_code != 200:
        return jsonify({'error': 'Unable to reach Message Service'}), 500
    
    # Parse response to find if message exists
    messages = message_check.json().get('messages', [])
    if message_id >= len(messages):
        return jsonify({'error': 'Message not found'}), 404
    
    # Add a like to the message
    if message_id not in likes:
        likes[message_id] = 0
    likes[message_id] += 1
    
    return jsonify({'message': f'Message {message_id} liked successfully'}), 200

# Route to get the number of likes for a message
@app.route('/likes/<int:message_id>', methods=['GET'])
def get_likes(message_id):
    if message_id not in likes:
        return jsonify({'likes': 0}), 200
    return jsonify({'likes': likes[message_id]}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)


