# Trello Backend Capstone

## Overview

This project is a Trello-style backend application built using FastAPI, PostgreSQL, SQLAlchemy and Alembic.
This project is a Trello-style backend application developed using FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, and JWT Authentication.

The application enables users to create and manage boards, sections, tickets, invitations, and board memberships while enforcing role-based access control.

### Key Features

* User Registration
* User Authentication (JWT)
* Board Management
* Section Management
* Ticket Management
* Board Invitations
* Board Membership
* Role-Based Access Control (RBAC)
* Unit & Integration Testing
* Dockerized Deployment

---

## Tech Stack

* Python 3.12
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Uvicorn
* Docker
* Docker Compose
* Nginx

---

## Project Structure

```text
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

tests/
├── unit/
└── integration/
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd trello-backend-capstone
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
PROJECT_NAME="Trello Backend Capstone"

POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=trello_capstone_db

DATABASE_URL=postgresql+asyncpg://your_username:your_password@localhost:5432/trello_capstone_db

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start Application

```bash
uvicorn app.main:app --reload
```

### 7. Open Swagger UI

```text
http://localhost:8000/docs
```

---

## Features

### Authentication

* Register User
* Login User
* JWT Protected Endpoints

### Boards

* Create Board
* List User Boards
* Board Details
* Board Membership

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
* Ticket Assignment

### Collaboration

* Generate Invitation Token
* Accept Invitation
* Manage Board Members

### Role-Based Access Control (RBAC)

#### Board Owner

* Manage Board
* Manage Sections
* Manage Members
* Manage All Tickets

#### Board Member

* Access Joined Boards
* Create Own Tickets
* Edit Own Tickets
* Delete Own Tickets

---

## Database Migrations

### Create Migration

```bash
alembic revision --autogenerate -m "migration_message"
```

### Apply Migrations

```bash
alembic upgrade head
```

---

## API Documentation

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

# API Usage Examples

## Register User

### Endpoint

```http
POST /api/v1/auth/register
```

### Request Body

```json
{
"email": "[user@test.com](mailto:user@test.com)",
"password": "password123",
"first_name": "John",
"last_name": "Doe"
}
```

---

## Login User

### Endpoint

```http
POST /api/v1/auth/login
```

### Content Type

```text
application/x-www-form-urlencoded
```

### Form Data

```text
username=user@test.com
password=password123
```

### Response

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

## Create Board

```http
POST /api/v1/boards/
```

```json
{
  "title": "Project Board",
  "description": "Capstone Board"
}
```

---

## Create Section

```http
POST /api/v1/sections/
```

```json
{
  "name": "To Do",
  "description": "Tasks to start",
  "board_id": "<board_id>"
}
```

---

## Create Ticket

```http
POST /api/v1/tickets/
```

```json
{
  "title": "Implement Login",
  "description": "JWT Authentication",
  "section_id": "<section_id>",
  "assignee_id": null
}
```

---

## Generate Invitation

```http
POST /api/v1/invitations/boards/<board_id>
```

---

## Accept Invitation

```http
POST /api/v1/invitations/accept/<token>
```

---

# Testing

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run All Tests

```bash
pytest
```

## Run Unit Tests

```bash
pytest tests/unit -v
```

## Run Integration Tests

```bash
pytest tests/integration -v
```

## Generate Coverage Report

```bash
pytest --cov=app --cov-report=term-missing
```

### Test Coverage

Current project coverage: **68%**

The project satisfies the capstone requirement of:

* At least 50% unit test coverage
* At least 50% endpoint/integration test coverage

---

# Docker Setup

## Docker Architecture

```text
Client
   │
   ▼
Nginx
   │
   ▼
FastAPI (Uvicorn)
   │
   ▼
PostgreSQL
```

## Containers

The application runs using three containers:

* FastAPI Backend (Uvicorn)
* PostgreSQL Database
* Nginx Reverse Proxy

## Build and Start Containers

```bash
docker compose up -d --build
```

## View Running Containers

```bash
docker ps
```

## View Logs

```bash
docker compose logs
```

## Stop Containers

```bash
docker compose down
```

## Rebuild Containers

```bash
docker compose up -d --build
```

---

## Capstone Requirements Implemented

### Part 1

* User Registration
* User Authentication
* Board Management
* Section CRUD
* Ticket CRUD
* Invitations
* Board Membership
* RBAC

### Part 2

* Unit Testing
* Integration Testing
* Coverage Reporting

### Part 3

* Dockerfile
* Docker Compose
* PostgreSQL Container
* FastAPI Container
* Nginx Container

---

## Author

Mohammed Junaid Shaik

Python Full Stack Intern

Grid Dynamics
