from pydantic import BaseModel

class NoteUpdateResponse(BaseModel):
    id: int
    title: str
    updated_at: int
    description: str | None = None