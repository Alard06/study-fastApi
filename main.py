from urllib.request import Request

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from starlette.responses import HTMLResponse, JSONResponse, Response, PlainTextResponse, FileResponse

app = FastAPI()


@app.get('/')
async def root():
    return FileResponse('public/index.html')


@app.get('/getText')
async def get_text():
    return FileResponse('public/test.txt',
                        media_type='application/octet-stream',
                        filename='public/test.txt')