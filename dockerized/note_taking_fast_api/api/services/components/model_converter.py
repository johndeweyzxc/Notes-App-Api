from api.models.note_get import NoteGet
from api.models.components.date_information import DateInformation

def convert_to_note_model(data: dict[str, any]) -> NoteGet:
    date_information = DateInformation(
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at'),
        deleted_at=data.get('deleted_at')
    )
    note_get = NoteGet(
        title=data.get('title'),
        description=data.get('description'),
        date_information=date_information
    )
    return note_get