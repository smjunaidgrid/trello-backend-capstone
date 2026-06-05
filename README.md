# Trello Backend Capstone

## Overview

This project is a Trello-style backend application built using FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

The application supports:

* User Registration
* User Authentication (JWT)
* Board Management
* Section Management
* Ticket Management
* Board Invitations
* Board Membership
* Role-Based Access Control (RBAC)

---

## Tech Stack

* Python 3.12
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Uvicorn

---

## Project Structure

app/
├── api/
├── models/
├── repositories/
├── schemas/
├── services/
├── db/
└── main.py

alembic/
└── versions/

---

## Setup Instructions

### 1. Clone Repository

git clone <repository-url>

cd trello-backend-capstone

### 2. Create Virtual Environment

python -m venv .venv

source .venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a .env file:

DATABASE_URL=postgresql+asyncpg://username:password@localhost/trello_capstone_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

### 5. Run Database Migrations

alembic upgrade head

### 6. Start Application

uvicorn app.main:app --reload

### 7. Open Swagger

http://localhost:8000/docs

---

## Features

### Authentication

* Register User
* Login User
* JWT Protected Endpoints

### Boards

* Create Board
* List Boards
* Board Details

### Sections

* Create Section
* Update Section
* Delete Section
* List Sections

### Tickets

* Create Ticket
* Update Ticket
* Delete Ticket
* List Tickets

### Collaboration

* Generate Invitation Token
* Accept Invitation
* Board Membership Management

### RBAC

Owner:

* Manage Board
* Manage Members
* Manage All Tickets

Member:

* View Joined Boards
* Create Own Tickets
* Edit Own Tickets
* Delete Own Tickets

---

## Database Migrations

Create migration:

alembic revision --autogenerate -m "message"

Apply migration:

alembic upgrade head

---

## API Documentation

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc


# API Usage Examples

## Register

POST /api/v1/auth/register

{
"email": "[user@test.com](mailto:user@test.com)",
"password": "password123",
"first_name": "John",
"last_name": "Doe"
}

---

## Login

POST /api/v1/auth/login

{
"email": "[user@test.com](mailto:user@test.com)",
"password": "password123"
}

Response:

{
"access_token": "...",
"token_type": "bearer"
}

---

## Create Board

POST /api/v1/boards/

{
"title": "Project Board",
"description": "Capstone Board"
}

---

## Create Section

POST /api/v1/sections/

{
"name": "To Do",
"description": "Tasks to start",
"board_id": "<board_id>"
}

---

## Create Ticket

POST /api/v1/tickets/

{
"title": "Implement Login",
"description": "JWT Authentication",
"section_id": "<section_id>",
"assignee_id": null
}

---

## Generate Invitation

POST /api/v1/invitations/boards/<board_id>

---

## Accept Invitation

POST /api/v1/invitations/accept/<token>


~ Mohammed Junaid Shaik
~ Intern - Python Full Stack
~ Grid Dynamics
