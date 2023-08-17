from components.test_get import test_get_note
from components.test_upload import test_upload_note
from components.test_update import test_update_note
from components.test_delete import test_delete_note
import json
import argparse

def compare_dictionary(dict1: dict[str, any], dict2: dict[str, any]):
    for key, value in dict1.items():
        if key == 'id' or key == 'date_information':
            continue

        if key not in dict2:
            return False

        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                if subvalue != dict2[key][subkey]:
                    return False
        else:
            if value != dict2[key]:
                return False
    return True

def verify_update_route():
    with open('api_tester/test_data/verify_update.json', 'r') as f:
        data = json.load(f)
    
    data_to_be_uploaded = data['data_to_be_uploaded']
    updated_data = data['updated_data']

    # First upload the data
    upload_status_code, _ = test_upload_note(
        optional_data=data_to_be_uploaded)
    assert upload_status_code == 201

    # Then update the data
    update_status_code, _ = test_update_note(
        optional_data=updated_data)
    assert update_status_code == 200

    # Get the data, the id is 1 so everytime we conduct this test, 
    # make sure to create new table.
    get_status_code, get_body = test_get_note(note_id=1)
    assert get_status_code == 200
    # Check if the data is updated
    assert compare_dictionary(updated_data, get_body) == True

def check_deleted_at(data):
    if data['date_information']['deleted_at'] is not None:
        return True
    else:
        return False

def verify_delete_route():
    with open('api_tester/test_data/verify_update.json', 'r') as f:
        data = json.load(f)
    
    data_to_be_uploaded = data['data_to_be_uploaded']

    # First check if data is in the database
    get_status_code, _ = test_get_note(note_id=1)
    assert get_status_code == 404

    # Then upload data
    upload_status_code, _ = test_upload_note(
        optional_data=data_to_be_uploaded)
    assert upload_status_code == 201

    # Delete the data
    delete_status_code, _ = test_delete_note(note_id=1)
    assert delete_status_code == 204

    # Fetch data again to know if it is truely deleted
    get_status_code2, get_body2 = test_get_note(note_id=1)
    assert get_status_code2 == 200
    assert check_deleted_at(get_body2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str, help='Enter the operation to be tested')
    args = parser.parse_args()
    operation = args.operation

    if operation == 'verify_update_route':
        verify_update_route()
    elif operation == 'verify_delete_route':
        verify_delete_route()