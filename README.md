# Data Dashboard App — Deployment Guide

This guide explains how to set up and run the project using Docker.

---

## Tech Stack

- Backend: Python, FastAPI, SQLAlchemy, Pydantic
- Frontend: React (Vite), TypeScript, Material UI
- Database: PostgreSQL
- Containerization: Docker & Docker Compose
- Tests: pytest, pytest-asyncio, httpx, aiosqlite


## Project Structure

```
├── backend/
├── frontend/
├── docker-compose.yml
```


## Prerequisites

Make sure you have installed:

- Docker
- Docker Compose

Check installation:

```bash
  docker --version
  docker compose version
```

If you haven't already installed them, you can download and install it from the [official Docker website](https://www.docker.com/get-started).


## Environment Variables

This project uses environment variables for configuration.

### Backend

Copy the example file:

```bash
  cp backend/.env.sample backend/.env
```

Then update values.

### Frontend

Copy the example file:

```bash
  cp frontend/.env.sample frontend/.env
```

Then update values.

## Docker Setup

### Running the Applications

1. You can run the applications using Docker Compose:
```bash
  docker-compose up --buid
```

2. By default, the backend application will be accessible at `http://localhost:5001` and frontend application at `http://localhost:5173` in your web browser. If you have configured different values in your `.env` files, make sure to access the applications using those settings.

### Stopping the Applications

To stop the running applications, you can use:
```bash
  docker-compose down
```

This command will stop and remove the containers created by `docker-compose up`.
