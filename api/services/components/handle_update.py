from datetime import datetime

def handle_update(note_update_dict: dict[str, any]):
    fields_to_update = {}
    fields_to_update['updated_at'] = int(datetime.now().timestamp())

    for key, value in note_update_dict.items():
        if key == 'id':
            continue
        if value is not None:
            fields_to_update[key] = value
    
    return fields_to_update