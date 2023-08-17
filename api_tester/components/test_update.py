import requests
import json
from api_const import BASE_URL, process_header_values
import pprint

def test_update_note(verbose=False, optional_data: dict[str, any]=None):
    endpoint = '/api/v1/update-note'

    with open('api_tester/test_data/update.json', 'r') as f:
        data_body = optional_data if optional_data != None else json.load(f)

    response = requests.patch(f'{BASE_URL}{endpoint}', json=data_body)
    if verbose: process_header_values(response.headers)
    body: str = response.content.decode('utf-8')
    if verbose: print(f'STATUS CODE: {response.status_code}\n')

    return (response.status_code, body)