from datetime import datetime

def handle_delete():
    fields_to_update = {}
    fields_to_update['deleted_at'] = int(datetime.now().timestamp())
    return fields_to_update