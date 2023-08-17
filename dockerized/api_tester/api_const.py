from dotenv import load_dotenv
import os

load_dotenv()

server_ip = os.getenv('SERVER_IP')
server_port = os.getenv('SERVER_PORT')

BASE_URL = f'http://{server_ip}:{(server_port)}'

def process_header_values(header: dict[str, str]):
    for key, value in header.items():
        print(f'{key}: {value}')