from api_const import BASE_URL, process_header_values
import requests

def test_delete_note(note_id: int, verbose=False):
    endpoint = f'/api/v1/delete-note/{note_id}'
    response = requests.delete(f'{BASE_URL}{endpoint}')
    if verbose: process_header_values(response.headers)
    if verbose: print(f'STATUS CODE: {response.status_code}\n')
    return (response.status_code, None)