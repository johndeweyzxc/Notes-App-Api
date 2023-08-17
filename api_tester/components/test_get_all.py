from api_const import BASE_URL, process_header_values
import json
import requests
import pprint

def test_get_all_note(verbose=False):
    endpoint = '/api/v1/get-all-note'
    response = requests.get(f'{BASE_URL}{endpoint}')
    if verbose: process_header_values(response.headers)

    body: str = response.content.decode('utf-8')
    data_list: list[dict[str, any]] = json.loads(body)
    
    if verbose: print(f'STATUS CODE: {response.status_code}\n')
    if verbose:
        pprint.pprint(data_list, indent=2)
    return (response.status_code, data_list['note_list'])