from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from app.database import get_db_connection, close_db_connection
import asyncio

async def homepage(request):
    connection = await get_db_connection()
    rows = await connection.fetch('SELECT * FROM image_data')  # Assuming you have a table 'documents'
    await close_db_connection(connection)
    documents = [dict(row) for row in rows]
    return JSONResponse(documents)

routes = [
    Route("/", homepage),
]

app = Starlette(debug=True, routes=routes)
