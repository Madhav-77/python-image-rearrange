from starlette.routing import Route
from app.views.image_view import get_image_data, update_image_data

routes = [
    Route("/api/images/get", get_image_data, methods=["GET"]),
    Route("/api/images/update", update_image_data, methods=["PATCH"]),
]
