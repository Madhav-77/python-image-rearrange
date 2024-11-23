import asyncpg
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Establish a connection pool
async def get_db_connection():
    connection = await asyncpg.connect(DATABASE_URL)
    return connection

# Close the connection
async def close_db_connection(connection):
    await connection.close()
