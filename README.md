# Job Tracker

FastAPI app for tracking job applications, with PostgreSQL via Docker Compose.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose

## Run the database with Docker

From the project root:

```bash
docker compose up -d
```

This starts PostgreSQL using the `postgres:17-alpine` image.

### Connection details

| Setting  | Value            |
|----------|------------------|
| Host     | `127.0.0.1`      |
| Port     | `5432`           |
| User     | `mac`            |
| Password | `Macsmith`       |
| Database | `jobtracker_db`  |

Connection URL:

```text
postgresql://mac:Macsmith@127.0.0.1:5432/jobtracker_db
```

### Useful commands

```bash
# Check status
docker compose ps

# View logs
docker compose logs -f db

# Open a Postgres shell
docker compose exec db psql -U mac -d jobtracker_db

# Inside psql, check the server version
# SELECT version();

# To see the database that you have, 
/l

# To see the database table that you have, 
/dt

# To get out of there, 
/q

# Stop containers (keeps data)
docker compose stop

# Start containers (keeps data)
docker compose start

# Stop and remove containers (keeps volume data)
docker compose down

# Stop and delete the database volume
docker compose down -v
```

Data is stored in the `postgres_data` Docker volume and persists across restarts.

## Run the API locally

With the database running, start the FastAPI backend from `backend/`:

```bash
cd backend
uv sync          # or: pip install -e .
fastapi dev app/main.py
```

API: http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs
