from pydantic import BaseModel

class NoteUploadResponse(BaseModel):
    id: int
    title: str
    created_at: int
    description: str | None = None