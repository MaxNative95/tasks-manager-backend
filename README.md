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

## Recommendations and Future Improvements

- Add user registration directly from the app.
- Validate forms and inputs on both frontend and backend.
- Implement better error handling and user feedback on the mobile app.
- Add loading spinners or skeletons for API calls.
- Improve token expiration handling and auto-logout.
- Use refresh tokens for better session management.
- Integrate push notifications for task reminders.
- Add due dates and priorities for tasks.
- Implement offline mode or optimistic UI for better UX.
- Improve UI/UX with design systems like Tailwind (web) or styled-components (mobile).
- Add unit and integration tests on both frontend and backend.
- Use environment-based configuration for production and development builds.
- Restrict CORS properly in the backend.
- Add user profile management (update email/password).
- Paginate or lazy-load task lists for scalability.
- Improve API error messages with standard error codes.
- Add Swagger/OpenAPI documentation to the FastAPI backend.
- Use role-based access control if supporting multiple user roles in the future.
- Deploy backend and frontend with CI/CD pipelines.
- Add analytics or logging tools for monitoring the app.
