import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import Error, MySQLConnection
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')
database_host = os.getenv('DATABASE_IP')
password = os.getenv('PASSWORD')
database_name = os.getenv('DATABASE_NAME')
database_port = os.getenv('DATABASE_PORT')

def connect_db(user_name: str, 
               host_name: str, 
               user_password: str, 
               db_name: str,
               db_port: int) -> MySQLConnection:
    name = 'connect_db()'
    connection = None
    try:
        connection: MySQLConnection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=db_port
        )
        print(f'\033[32mINFO\033[0m: {name}: Connected to mysql server')
    except Error as err:
        print(f"\033[31mERROR\033[0m: {name}: {err}")
        print(f'\033[32mINFO\033[0m: {name}: Closing database connection')

    return connection

def sql_exec_read_query(query: str, data: tuple) -> (dict[str, any], int):
    name = 'sql_exec_read_query()'
    connection: MySQLConnection = connect_db(
        username, database_host, password, database_name, int(database_port))
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        print(f'\033[32mINFO\033[0m: {name}: Query -> {query}')
        list_data = None if data is None else data
        
        cursor.execute(query, list_data)
        result = cursor.fetchall()
    
        print(f'\033[32mINFO\033[0m: {name}: Closing database connection')
        connection.close()
        return ( result, 0)
    except Error as err:
        print(f"\033[31mERROR\033[0m: {name}: {err}")
        print(f'\033[32mINFO\033[0m: {name}: Closing database connection')
        connection.close()
        return ( [], 1 )

def sql_exec_write_query(query: str, data: tuple) -> int:
    name = 'sql_exec_write_query()'
    connection: MySQLConnection = connect_db(
        username, database_host, password, database_name, int(database_port))
    cursor: MySQLCursor = connection.cursor()
    try:
        print(f'\033[32mINFO\033[0m: {name}: Query -> {query}')
        list_data = data if data is not None else ()

        cursor.execute(query, list_data)
        connection.commit()
        print(f'\033[32mINFO\033[0m: {name}: Closing database connection')
        connection.close()
        return (cursor.lastrowid, 0)
    except Error as err:
        print(f"\033[31mERROR\033[0m: {name}: {err}")
        print(f'\033[32mINFO\033[0m: {name}: Closing database connection')
        connection.close()
        return 1

def create_table(table_name: str):
    query = f"""
    CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        created_at INT UNSIGNED,
        updated_at INT UNSIGNED, 
        deleted_at INT UNSIGNED
    );"""
    sql_exec_write_query(query, None)

def drop_table(table_name: str):
    query = f'DROP TABLE {table_name};'
    sql_exec_write_query(query, None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task', type=str, help='Enter the task to be executed')
    parser.add_argument('table_name', type=str, help='Enter the target table')

    args = parser.parse_args()
    task = args.task
    table_name = args.table_name

    if task == 'create_table':
        create_table(table_name)
    elif task == 'drop_table':
        drop_table(table_name)
