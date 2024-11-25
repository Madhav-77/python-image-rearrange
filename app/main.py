from starlette.applications import Starlette
from app.middlewares import page_not_found_middleware
from app.routes import routes

app = Starlette(debug=True, routes=routes)

page_not_found_middleware(app)
