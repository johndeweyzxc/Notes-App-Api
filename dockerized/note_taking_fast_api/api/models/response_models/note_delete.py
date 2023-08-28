from pydantic import BaseModel

class NoteDelete(BaseModel):
    deleted_at: int