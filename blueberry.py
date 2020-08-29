import os
import configparser
from sanic import Sanic
from sanic import response
# from werkzeug.utils import secure_filename
from domonic.html import *
from domonic.terminal import ls

from app import *
from app.components import *


app = Sanic(name='Blueberry OS')
app.static('/assets', './assets')

# to customise update the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
profile = 'default'
app.config['DESKTOP'] = config.get(profile,'DESKTOP', fallback='.')
app.config['IS_ROOT'] = config.get(profile,'IS_ROOT', fallback=True)
app.config['UPLOAD_DIR'] = config.get(profile,'UPLOAD_DIR', fallback='./Uploads')
# app.config['WALLPAPER'] = config.get(profile,'WALLPAPER', fallback='')
# dock --
app.config['TWITTER'] = config.get(profile,'TWITTER', fallback='tim_cook')
app.config['GITHUB'] = config.get(profile,'GITHUB', fallback='byteface')
app.config['WEBSITE'] = config.get(profile,'WEBSITE', fallback='https://github.com/apple')
# app.config['CV'] = config.get(profile,'CV', fallback="")
app.config['LINKEDIN'] = config.get(profile,'LINKEDIN', fallback="https://www.linkedin.com/company/apple/")
# app.config['SPOTIFY'] = config.get(profile,'SPOTIFY', fallback=0)



# returns a specific component to be re-rendered
@app.route('/file')
async def file(request):
    return response.html( str(Pad(request.args['file'][0], request.args['id'][0])) )

# returns a specific component to be re-rendered
@app.route('/dir')
async def dir(request):
    return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )


# @app.route("/template", methods=["POST"])
# def template():
# TODO - need to write a 'decorator' that maps request params into a domonic components constructor
# ideally it would DI the app context as well as the request. or will need to create template methods to pass refs through 
@app.route("/component")
async def component(request):
    try:  # TODO - fix these up rather than bodging thru now that its sorted further below...
        return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )
    except Exception as e:
        print(e)
        return response.html( str(Pad(request.args['file'][0], request.args['id'][0])) )


# Component - A 'component' takes a request as input and returns html
@app.route("/component/<component>")
async def component2(request, component):
    try:
        module = __import__(f'app.components.{component}')
        my_class = getattr(module, component.title())
        return response.html( str( my_class(request) ) )
    except Exception as e:
        print(e)
        return response.html( str( div("COMPONENT NOT FOUND!") ) )


@app.route('/upload', methods=['POST'])
async def upload(request):
        if not os.path.exists(app.config.UPLOAD_DIR): os.makedirs(app.config.UPLOAD_DIR)
        upload_file = request.files.get('file')
        filename = upload_file.name
        with open(app.config.UPLOAD_DIR+"/"+filename, "wb") as f:
            # TODO - async with aiofiles.open(path, 'wb') as f: await f.write(body)
            f.write(upload_file.body)
            f.close()


@app.route('/')
async def test(request):
    page = render(html('<!DOCTYPE HTML>', hd, bd, _lang="en-US", _class="no-js"))
    return response.html( page )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
