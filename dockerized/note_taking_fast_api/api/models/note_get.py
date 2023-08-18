from pydantic import BaseModel
from api.models.components.date_information import DateInformation

class NoteGet(BaseModel):
    title: str
    description: str | None = None
    date_information: DateInformation