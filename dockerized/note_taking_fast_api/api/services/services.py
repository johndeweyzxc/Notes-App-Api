from api.repository.repository import sql_get_note, sql_get_all_note
from api.repository.repository import sql_update_note, sql_upload_note
from api.repository.repository import sql_delete_note
from api.models.response_models.note_get import NoteGet
from api.models.response_models.note_get_all import NoteGetAll
from api.models.note_update import NoteUpdate
from api.models.note_upload import NoteUpload
from api.models.response_models.note_update import NoteUpdateResponse
from api.models.response_models.note_upload import NoteUploadResponse
from api.models.response_models.note_delete import NoteDelete
from api.services.components.model_converter import convert_to_note_model
from api.services.components.handle_update import handle_update
from api.services.components.handle_upload import handle_upload
from api.services.components.handle_delete import handle_delete
from fastapi import status

def service_get_note(note_id: int):
    data, status_code = sql_get_note(note_id)
    
    if len(data) > 1 or status_code != status.HTTP_200_OK:
        return (None, status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif len(data) == 0:
        return ([], status.HTTP_404_NOT_FOUND)
    
    data = data[0]
    model: NoteGet = convert_to_note_model(data)
    return (model, status.HTTP_200_OK)

def service_get_all_note():
    data, status_code = sql_get_all_note()
    
    if status_code != status.HTTP_200_OK:
        return (None, status.HTTP_500_INTERNAL_SERVER_ERROR)

    list_of_note: list[NoteGet] = []
    for note in data:
        note_get: NoteGet = convert_to_note_model(note)
        list_of_note.append(note_get)
    
    note_list = NoteGetAll(note_list=list_of_note)
    return (note_list, status.HTTP_200_OK)

def service_update_note(note_update: NoteUpdate):
    note_update_dict: dict[str, any] = note_update.__dict__
    note_id = note_update_dict.get('id')
    data_to_update = handle_update(note_update_dict)
    db_status = sql_update_note(data_to_update, note_id)

    response_data = NoteUpdateResponse(
        id=note_id, 
        title=data_to_update.get("title"),
        updated_at=data_to_update.get("updated_at"),
        description=data_to_update.get("description"),
        )

    return (response_data, db_status)

def service_upload_note(note_upload: NoteUpload):
    note_upload_dict: dict[str, any] = note_upload.__dict__
    data_to_upload = handle_upload(note_upload_dict)
    last_row_id, db_status = sql_upload_note(data_to_upload)

    response_data = NoteUploadResponse(
        id=last_row_id,
        title=data_to_upload.get("title"),
        created_at=data_to_upload.get("created_at"),
        description=data_to_upload.get("description")
    )

    return (response_data, db_status)

def service_delete_note(note_id: int):
    data_to_update = handle_delete()
    db_status = sql_delete_note(data_to_update, note_id)

    response_data = NoteDelete(deleted_at=data_to_update.get("deleted_at"))
    return (response_data, db_status)