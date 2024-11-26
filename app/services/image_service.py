import asyncpg
from app.models import ImageData
from typing import List

# service to get and update data in database
class ImageService:
    def __init__(self, db_connection: asyncpg.Connection):
        self.db_connection = db_connection

    async def get_image_data(self) -> List[ImageData]:
        
        # get all image data ordered by position
        query = 'SELECT * FROM image_data ORDER BY position ASC'
        rows = await self.db_connection.fetch(query)
        return [ImageData(**dict(row)) for row in rows] # strict data type check with ImageData

    async def update_image_position(self, image_id: int, position: int) -> ImageData:
        
        # update the position of a single image by id
        query = """ UPDATE image_data SET position = $1 WHERE id = $2 RETURNING *; """
        row = await self.db_connection.fetchrow(query, position, image_id)
        if row:
            return ImageData(**dict(row))
        return None

    async def update_multiple_image_positions(self, update_data: List[ImageData]) -> List[ImageData]:
        
        # update positions for multiple images in one go
        updated_images = []
        for item in update_data:
            updated_image = await self.update_image_position(item.id, item.position)
            if updated_image:
                updated_images.append(updated_image)
        return updated_images
