import os
import configparser  # TODO - switch to toml

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from domonic.html import *
from domonic.terminal import ls
from app import *
# from app.components import Pad, Peruser
from app.components import *

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/static", StaticFiles(directory="static"), name="static")

# TODO - app.config.UPLOAD_DIR = "uploads"


@app.get('/file')
async def file(file: str, id: str):
    """returns a specific component to be re-rendered"""
    return HTMLResponse(str(Pad(file, id)))


@app.get('/dir')
async def dir(directory: str, id: str):
    """returns a specific component to be re-rendered"""
    return HTMLResponse(str(Peruser(directory, id)))


# @app.get("/template", methods=["POST"])
# def template():
# TODO - need to write a 'decorator' that maps request params into a domonic components constructor
# ideally it would DI the app context as well as the request. or will need to create template methods to pass refs through 
@app.get("/component")
async def component(directory: str = None, id: str = None, file: str = None):
    try:  # TODO - fix these up rather than bodging thru now that its sorted further below...
        return HTMLResponse(str(Peruser(directory, id)))
    except Exception as e:
        print(e)
        return HTMLResponse(str(Pad(file, id)))


# Component - takes a request as input and returns html
@app.get("/component/{component}/")
async def component2(component, request: Request = None):
    params = request.query_params
    try:
        module = __import__(f'app.components.{component}')
        my_class = getattr(module, component.title())
        return HTMLResponse(str(my_class(params)))
    except Exception as e:
        print(e)
        return HTMLResponse(str(div("COMPONENT NOT FOUND!")))


# @app.get('/upload', methods=['POST'])
# async def upload(request):
#     if not os.path.exists(app.config.UPLOAD_DIR): os.makedirs(app.config.UPLOAD_DIR)
#     upload_file = request.files.get('file')
#     filename = upload_file.name
#     with open(app.config.UPLOAD_DIR+"/"+filename, "wb") as f:
#         f.write(upload_file.body)
#         f.close()
#     return HTMLResponse( "done" )

@app.get('/')
async def test():
    return HTMLResponse(str(html('<!DOCTYPE HTML>', hd, bd, _lang="en-US", _class="no-js")))


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
