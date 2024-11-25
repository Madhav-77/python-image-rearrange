import asyncpg
from app.database import get_db_connection
from app.services.image_service import ImageService
from app.models import ImageData
from starlette.responses import JSONResponse
from starlette.requests import Request

# view that retrieves image data
async def get_image_data(request: Request):
    try:
        async with get_db_connection() as connection:
            
            # instantiate the ImageService with the connection
            image_service = ImageService(connection)
            images = await image_service.get_image_data()
            return JSONResponse([image.dict() for image in images], status_code=200)

    except asyncpg.PostgresError as e:
        return JSONResponse({"error": f"Database error: {str(e)}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": f"Unexpected error: {str(e)}"}, status_code=500)

# view that updates the position of images
async def update_image_data(request: Request):
    try:
        data = await request.json()
        update_data = [ImageData(**item) for item in data] # strict data type check with ImageData

        async with get_db_connection() as connection:
            
            # instantiate the ImageService with the connection
            image_service = ImageService(connection)
            updated_images = await image_service.update_multiple_image_positions(update_data)

            if not updated_images:
                return JSONResponse({"error": "No images were updated."}, status_code=404)

            return JSONResponse([image.dict() for image in updated_images], status_code=200)

    except asyncpg.PostgresError as e:
        return JSONResponse({"error": f"Database error: {str(e)}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": f"Unexpected error: {str(e)}"}, status_code=500)
