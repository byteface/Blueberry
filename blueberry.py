from sanic import Sanic
from sanic import response
from domonic.html import *
from domonic.terminal import ls
from app import *

app = Sanic(name='Blueberry OS')
app.static('/assets', './assets')

# returns a specific component to be re-rendered
@app.route('/file')
async def file(request):
    return response.html( str(Pad(request.args['file'][0], request.args['id'][0])) )

# returns a specific component to be re-rendered
@app.route('/dir')
async def dir(request):
    return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )


# Component route
# @app.route("/component/<component>")
# def component(component):
@app.route("/component")
async def component(request):
        # TODO - dynamic load components. think its something like this... i.e. pypal    
        # from domonic.components import *
        # module = __import__(component)
        # reload(module)
        # return response.html( str( command_module(request.args) ) )
    try:
        return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )
    except Exception as e:
        return response.html( str(Pad(request.args['file'][0], request.args['id'][0])) )

@app.route('/')
async def test(request):
    page = render(html('<!DOCTYPE HTML>', hd, bd, _lang="en-US", _class="no-js"))
    return response.html( page )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
