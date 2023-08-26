from pydantic import BaseModel

class NoteUpdate(BaseModel):
    id: int
    title: str
    created_at: int
    description: str | None = None