import asyncio

import uvicorn
from fastapi import FastAPI

from cmd import router, consumer



app = FastAPI()


@app.get('/')
async def Home():
    return 'welcome home'

app.include_router(router.route)
asyncio.create_task(consumer.consume())


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8000, reload=True)
