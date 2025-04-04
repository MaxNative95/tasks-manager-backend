# Task Manager - Backend

Task Manager API is a secure backend built with FastAPI and MongoDB. It provides JWT-authenticated endpoints to manage personal tasks per user.
Go here to test the api in local env ----> http://127.0.0.1:8000/docs#/

## Technologies
- FastAPI
- MongoDB (with Motor)
- Pydantic
- python-jose (JWT)
- Uvicorn
- Docker
- Mangum (optional for AWS Lambda)

## Getting Started

1. Clone the repository:
git clone git@github.com:MaxNative95/tasks-manager-backend.git


2. Create a `.env` file with:
MONGODB_URI=mongodb://localhost:27017 SECRET_KEY=your_secret_key_here

3. Run with Docker Compose:
docker-compose up --build


## API Overview

This will start:
- FastAPI backend on `http://localhost:8000`
- MongoDB database

## API Overview

- `POST /register`: Register a new user
- `POST /login`: Login and receive JWT token
- `GET /tasks`: Get tasks for the authenticated user
- `POST /tasks`: Create a new task (user-bound)
- `PUT /tasks/{id}`: Update a task if owned by the user
- `DELETE /tasks/{id}`: Delete a task if owned by the user

## Notes

- All `/tasks` endpoints require a valid Bearer token.
- Each task is assigned to the user who created it.
- Users can only manage their own tasks.
