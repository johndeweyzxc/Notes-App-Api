from pydantic import BaseModel

class NoteUpload(BaseModel):
    title: str
    description: str | None = None