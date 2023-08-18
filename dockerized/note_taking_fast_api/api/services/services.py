from api.repository.repository import sql_get_note, sql_get_all_note
from api.repository.repository import sql_update_note, sql_upload_note
from api.repository.repository import sql_delete_note
from api.models.note_get import NoteGet
from api.models.note_get_all import NoteGetAll
from api.models.note_update import NoteUpdate
from api.models.note_upload import NoteUpload
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
    return sql_update_note(data_to_update, note_id)

def service_upload_note(note_upload: NoteUpload):
    note_upload_dict: dict[str, any] = note_upload.__dict__
    data_to_upload = handle_upload(note_upload_dict)
    return sql_upload_note(data_to_upload)

def service_delete_note(note_id: int):
    data_to_update = handle_delete()
    return sql_delete_note(data_to_update, note_id)