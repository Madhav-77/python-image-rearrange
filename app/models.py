from pydantic import BaseModel

class ImageData(BaseModel):
    id: int
    type: str
    title: str
    position: int