# Trello Backend Capstone

A production-oriented **Trello-style REST API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, **Docker**, and **JWT Authentication**. The application enables teams to manage boards, sections, tickets, invitations, and board memberships through secure REST APIs following a layered architecture.

This project was developed as part of the **Grid Dynamics Python Full Stack Internship – Module 10 Capstone Project**.

---

# Features

## User Authentication

* User Registration
* Secure Login using JWT Authentication
* Password Hashing
* Protected API Endpoints

## Board Management

* Create Board
* Update Board
* Delete Board
* List User Boards
* Board Details

## Section Management

* Create Section
* Update Section
* Delete Section
* List Sections within a Board

## Ticket Management

* Create Ticket
* Update Ticket
* Delete Ticket
* Move Ticket Between Sections
* Assign Ticket to Users

## Collaboration

* Board Invitations
* Invitation Acceptance
* Board Membership Management

## Authorization

Role-Based Access Control (RBAC)

### Board Owner

* Full Board Management
* Manage Members
* Manage Sections
* Manage All Tickets

### Board Member

* Access Joined Boards
* Create Own Tickets
* Update Own Tickets
* Delete Own Tickets

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy (Async ORM)
* Alembic
* Pydantic
* Uvicorn

## Database

* PostgreSQL

## Authentication

* JWT Authentication
* Passlib Password Hashing

## Testing

* Pytest
* HTTPX
* Async Testing

## Containerization

* Docker
* Docker Compose
* Nginx Reverse Proxy

## Cloud Deployment

* Amazon EC2
* Amazon RDS PostgreSQL
* Amazon VPC
* AWS Security Groups

---

# System Architecture

```text
                Client / Swagger UI
                        │
                        ▼
             FastAPI (Uvicorn Server)
                        │
                Service Layer
                        │
              Repository Layer
                        │
         SQLAlchemy Async ORM
                        │
                PostgreSQL Database
```

---

# AWS Deployment Architecture

```text
                Client
                   │
                   ▼
         Amazon EC2 Instance
      FastAPI + Uvicorn Server
                   │
         Security Group (5432)
                   │
                   ▼
      Amazon RDS PostgreSQL
```

---

# Project Structure

```text
trello-backend-capstone/
│
├── alembic/
│   └── versions/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│   ├── integration/
│   └── unit/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── README.md
└── .gitignore
```

---

# Local Installation

## Clone Repository

```bash
git clone https://github.com/smjunaidgrid/trello-backend-capstone.git

cd trello-backend-capstone
```

---

## Create Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
PROJECT_NAME="Trello Backend Capstone"

POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=trello

DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/trello

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Database Migration

Run Alembic migrations

```bash
alembic upgrade head
```

Create new migration

```bash
alembic revision --autogenerate -m "migration_name"
```

---

# Running the Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Docker Deployment

Build containers

```bash
docker compose up -d --build
```

View containers

```bash
docker ps
```

View logs

```bash
docker compose logs
```

Stop containers

```bash
docker compose down
```

---

# AWS Cloud Deployment

The backend application was successfully deployed to Amazon Web Services (AWS).

## Infrastructure

* Amazon EC2 (Application Server)
* Amazon RDS PostgreSQL
* Amazon VPC
* AWS Security Groups

Deployment validation included:

* EC2 instance provisioning
* PostgreSQL connectivity verification
* Alembic migration execution
* FastAPI deployment using Uvicorn
* Successful API execution against Amazon RDS

---

# API Overview

## Authentication

| Method | Endpoint                |
| ------ | ----------------------- |
| POST   | `/api/v1/auth/register` |
| POST   | `/api/v1/auth/login`    |

---

## Boards

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | `/api/v1/boards`      |
| GET    | `/api/v1/boards`      |
| GET    | `/api/v1/boards/{id}` |
| PUT    | `/api/v1/boards/{id}` |
| DELETE | `/api/v1/boards/{id}` |

---

## Sections

| Method | Endpoint                |
| ------ | ----------------------- |
| POST   | `/api/v1/sections`      |
| GET    | `/api/v1/sections`      |
| PUT    | `/api/v1/sections/{id}` |
| DELETE | `/api/v1/sections/{id}` |

---

## Tickets

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | `/api/v1/tickets`      |
| GET    | `/api/v1/tickets`      |
| PUT    | `/api/v1/tickets/{id}` |
| DELETE | `/api/v1/tickets/{id}` |

---

## Invitations

| Method | Endpoint                                |
| ------ | --------------------------------------- |
| POST   | `/api/v1/invitations/boards/{board_id}` |
| POST   | `/api/v1/invitations/accept/{token}`    |

---

# Testing

Install dependencies

```bash
pip install -r requirements.txt
```

Run all tests

```bash
pytest
```

Run unit tests

```bash
pytest tests/unit -v
```

Run integration tests

```bash
pytest tests/integration -v
```

Generate coverage report

```bash
pytest --cov=app --cov-report=term-missing
```

---

# Capstone Requirements

## Part 1

* User Registration
* User Authentication
* Board Management
* Section CRUD
* Ticket CRUD
* Invitation Management
* Board Membership
* Role-Based Access Control

## Part 2

* Unit Tests
* Integration Tests
* Test Coverage

## Part 3

* Dockerfile
* Docker Compose
* FastAPI Container
* PostgreSQL Container
* Nginx Reverse Proxy

## Part 4

* AWS Cloud Deployment
* Amazon EC2
* Amazon RDS PostgreSQL
* Secure Networking using Security Groups
* Database Migration using Alembic
* Cloud Database Connectivity Validation

## Part 5 (Proposed Enhancement)

Future CI/CD implementation using GitHub Actions:

* Pull Request Validation
* Automated Unit Testing
* Docker Image Build
* Container Registry Push
* Automated Cloud Deployment

---

# Future Enhancements

* React Frontend
* Kanban Drag-and-Drop Interface
* Redis Caching
* Email Notifications
* Background Workers
* WebSockets
* Application Load Balancer
* Auto Scaling Group
* Multi-Region Deployment
* Infrastructure as Code (Terraform)
* GitHub Actions CI/CD Pipeline

---

# Author

**Mohammed Junaid Shaik**

Python Full Stack Intern

Grid Dynamics
