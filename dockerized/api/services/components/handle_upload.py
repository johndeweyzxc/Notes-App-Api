from datetime import datetime

def handle_upload(note_upload_dict: dict[str, any]):
    fields_to_upload = {}
    fields_to_upload['created_at'] = int(datetime.now().timestamp())

    for key, value in note_upload_dict.items():
        if value is not None:
            fields_to_upload[key] = value
    
    return fields_to_upload