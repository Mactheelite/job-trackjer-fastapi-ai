This is how i initialized my uv

uv init backend --no-package --python 3.13.0

uv add "fastapi[standard]"
Note: Make sure you put "fastapi[standard]" in quotes to ensure it works in all terminals.

uv add "sqlalchemy[asyncio]" asyncpg

# To remove .git we use
rm -rf .git