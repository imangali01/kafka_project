import asyncio
import uvicorn
from cmd.main import app
from cmd.consumer import consume



async def startup_event():
    asyncio.create_task(consume())


app.add_event_handler("startup", startup_event)
