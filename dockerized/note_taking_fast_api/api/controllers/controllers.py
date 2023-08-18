from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from ..models.note_get import NoteGet
from ..models.note_get_all import NoteGetAll
from ..models.note_update import NoteUpdate
from ..models.note_upload import NoteUpload
from ..services.services import service_get_note, service_get_all_note, service_delete_note
from ..services.services import service_update_note, service_upload_note

note_taking_api_router = APIRouter()

@note_taking_api_router.get('/')
async def root():
    return {'message': 'Welcome to rest note taking api.'}

@note_taking_api_router.get('/api/v1/get-note/{note_id}', 
                            response_model=NoteGet,
                            status_code=status.HTTP_200_OK)
async def get_note(note_id: int):
    data, status_code = service_get_note(note_id)
    if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(content={"message": "Internal server error"}, status_code=status_code)
    elif status_code == status.HTTP_404_NOT_FOUND:
        return JSONResponse(content={"message": "Account not found"}, status_code=status_code)
    else:
        return data

@note_taking_api_router.get('/api/v1/get-all-note', 
                            response_model=NoteGetAll,
                            status_code=status.HTTP_200_OK)
async def get_all_note():
    data, status_code = service_get_all_note()
    if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(content={"message": "Internal server error"}, status_code=status_code)
    else:
        return data

@note_taking_api_router.patch('/api/v1/update-note',
                              status_code=status.HTTP_200_OK)
async def update_note(note_update: NoteUpdate):
    status_code = service_update_note(note_update)
    if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(content={"message": "Internal server error"}, status_code=status_code)

@note_taking_api_router.post('/api/v1/upload-note',
                             status_code=status.HTTP_201_CREATED)
async def upload_note(note_upload: NoteUpload):
    status_code = service_upload_note(note_upload)
    if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(content={"message": "Internal server error"}, status_code=status_code)

@note_taking_api_router.delete('/api/v1/delete-note/{note_id}',
                               status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    status_code = service_delete_note(note_id)
    if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        return JSONResponse(content={"message": "Internal server error"}, status_code=status_code)