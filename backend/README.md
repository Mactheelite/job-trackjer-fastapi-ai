This is how i initialized my uv

uv init backend --no-package --python 3.13.0

uv add "fastapi[standard]"
Note: Make sure you put "fastapi[standard]" in quotes to ensure it works in all terminals.

uv add "sqlalchemy[asyncio]" asyncpg

# To remove .git we use
rm -rf .git

# this help us to make migration when we create table
uv add alembic

run: uv run alembic init -t async alembic

uv run alembic revision --autogenerate -m "create users table"

uv run alembic upgrade head