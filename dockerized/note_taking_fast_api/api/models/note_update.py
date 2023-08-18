from pydantic import BaseModel

class NoteUpdate(BaseModel):
    id: int
    title: str
    description: str | None = None