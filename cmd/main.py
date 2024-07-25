from fastapi import FastAPI
from cmd import router



app = FastAPI()


@app.get('/')
async def Home():
    return 'welcome home'

app.include_router(router.route)
