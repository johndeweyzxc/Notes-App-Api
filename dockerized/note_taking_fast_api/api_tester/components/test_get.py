import requests
import json
from api_const import BASE_URL, process_header_values
import pprint

def test_get_note(note_id: int, verbose=False):
    endpoint = f'/api/v1/get-note/{note_id}'
    response = requests.get(f'{BASE_URL}{endpoint}')
    if verbose: process_header_values(response.headers)

    body: str = response.content.decode('utf-8')
    data = json.loads(body)
    if verbose: print(f'STATUS CODE: {response.status_code}\n')
    if verbose:
        pprint.pprint(data, indent=2)
    return (response.status_code, data)