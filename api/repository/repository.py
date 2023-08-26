from api.repository.sql_operation import sql_exec_read_query
from api.repository.sql_operation import sql_exec_write_query
from fastapi import status
from dotenv import load_dotenv
import os

load_dotenv()
table_name = os.getenv('TABLE_NAME')

def sql_update_note(data_to_update: dict[str, any], note_id: int):
    query = f'UPDATE {table_name} SET '
    new_values = []

    for index, (key, value) in enumerate(data_to_update.items()):
        len_data = len(data_to_update)
        query += f'{key} = %s' if index == (len_data - 1) else f'{key} = %s,'
        new_values.append(value)
    
    new_values.append(note_id)
    query += ' WHERE id = %s;'
    db_status = sql_exec_write_query(query,tuple(new_values))

    if db_status == 1:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return status.HTTP_200_OK

def sql_upload_note(new_data: dict[str, any]):
    query = f'INSERT INTO {table_name} '
    columns = ''
    placeholders = ''
    data = []

    for index, (key, value) in enumerate(new_data.items()):
        if index == len(new_data) - 1:
            columns += key
            placeholders += '%s'
        else:
            columns += f'{key},'
            placeholders += '%s,'
        
        data.append(value)
    
    query += f'({columns}) VALUES ({placeholders});'
    last_row_id, db_status = sql_exec_write_query(query, tuple(data))
    
    if db_status == 1:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return (last_row_id, status.HTTP_201_CREATED)

def sql_get_note(note_id: int):
    query = f'SELECT * FROM {table_name} WHERE id = %s;'
    id_list = [note_id]
    data, db_status = sql_exec_read_query(query, tuple(id_list))
    
    if db_status == 1:
        return (None, status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return (data, status.HTTP_200_OK)

def sql_get_all_note():
    query = f'SELECT * FROM {table_name}'
    data, db_status = sql_exec_read_query(query,None)

    if db_status == 1:
        return ([], status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return (data, status.HTTP_200_OK)

def sql_delete_note(data_to_update: dict[str, any], note_id: int):
    query = f'UPDATE {table_name} SET '
    data = []
    
    for index, (key, value) in enumerate(data_to_update.items()):
        len_data = len(data_to_update)
        query += f'{key} = %s' if index == (len_data - 1) else f'{key} = %s,'
        data.append(value)
    
    data.append(note_id)
    query += ' WHERE id = %s;'
    db_status = sql_exec_write_query(query, tuple(data))
    
    if db_status == 1:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return status.HTTP_204_NO_CONTENT