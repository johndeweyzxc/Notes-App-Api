from pydantic import BaseModel
from api.models.response_models.note_get import NoteGet

class NoteGetAll(BaseModel):
    note_list: list[NoteGet]