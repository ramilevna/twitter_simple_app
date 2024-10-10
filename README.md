# Twitter-Like System

This project implements a Twitter-like system using a service-based architecture. The system consists of three independent services: User Service, Message Service, and Like Service. Users can register, post short messages, read messages, and like them.

## Architecture Overview

- **User Service**: Manages user registration.
- **Message Service**: Handles posting and retrieving messages.
- **Like Service**: Manages likes for messages.

## Requirements

- Docker
- Docker Compose

## Project Structure

```
/project-root
│
├── /user-service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── user_service.py
│
├── /message-service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── message_service.py
│
├── /like-service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── like_service.py
│
└── docker-compose.yml
```


## Installation

1. Clone the repository.

2. Build and run the services using Docker Compose:
    ```bash
    docker-compose up --build
    ```

This command will build the Docker images and start the services on their respective ports.

## API Endpoints

### User Service

- **Register a User**:
  - **Endpoint**: `POST /register`
  - **Request Body**:
    ```json
    {
      "username": "your_username"
    }
    ```

### Message Service

- **Post a Message**:
  - **Endpoint**: `POST /messages`
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "content": "Your message content here"
    }
    ```

- **Get Messages Feed**:
  - **Endpoint**: `GET /messages`
  - **Response**:
    ```json
    {
      "messages": [
        {
          "id": 0,
          "username": "your_username",
          "content": "Your message content here"
        },
        ...
      ]
    }
    ```

### Like Service

- **Like a Message**:
  - **Endpoint**: `POST /likes/{messageId}`

- **Get Likes for a Message**:
  - **Endpoint**: `GET /likes/{messageId}`
  - **Response**:
    ```json
    {
      "likes": 0
    }
    ```

## Testing the Services

You can test the services using `curl` or any API testing tool (e.g., Postman). Here are some examples:

1. **Register a user**:
    ```bash
    curl -X POST http://localhost:5001/register -H "Content-Type: application/json" -d '{"username": "john_doe"}'
    ```

2. **Check if User is Registered**:
    ```bash
    curl -X GET http://localhost:5001/users/john_doe
    ```

3. **Post a Message (as a registered user)**:
    ```bash
    curl -X POST http://localhost:5002/messages -H "Content-Type: application/json" -d '{"username": "john_doe", "content": "Hello, world!"}'
    ```

4. **Post a Message (as an unregistered user)**:
    ```bash
    curl -X POST http://localhost:5002/messages -H "Content-Type: application/json" -d '{"username": "unknown_user", "content": "This should fail"}'
    ```

5. **Get the Last 10 Messages**:
    ```bash
    curl -X GET http://localhost:5002/messages
    ```
    
6. **Like a Message**:
    ```bash
    curl -X POST http://localhost:5003/likes/0
    ```

7. **Get the Number of Likes for a Message**:
    ```bash
    curl -X GET http://localhost:5003/likes/0
    ```
