import asyncpg
import asyncio
from dotenv import load_dotenv
import os
from contextlib import asynccontextmanager

# load environment variables from .env
load_dotenv(override=True)

DATABASE_URL = os.getenv('DATABASE_URL')

# initiate database connection
@asynccontextmanager
async def get_db_connection():
    connection = await asyncpg.connect(DATABASE_URL)
    try:
        yield connection
    finally:
        await connection.close()

# for closing the connection manually
async def close_db_connection(connection):
    await connection.close()
