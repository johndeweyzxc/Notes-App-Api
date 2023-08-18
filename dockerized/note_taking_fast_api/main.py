from fastapi import FastAPI
from api.controllers.controllers import note_taking_api_router
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

server_ip = os.getenv('SERVER_IP')
server_port = os.getenv('SERVER_PORT')

app = FastAPI()
app.include_router(note_taking_api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=server_ip, port=int(server_port), reload=True)
