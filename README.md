<h1 align="center">
    <img src="https://github.com/byteface/Blueberry/blob/master/assets/img/pie.jpg"
    style="background-color:rgba(0,0,0,0);" height=230 alt="Blueberry: browser based OS">
    <br>
    Blueberry π
    <br>
    <sup><sub><sup>Browser based file browser with Domonic and Sanic</sup></sub></sup>
    <br>
</h1>

# Blueberry π
##### built with domonic and sanic

##### setup
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -r requirements.txt

##### running
    python3 blueberry.py

##### customising

edit the congi.ini << NOT HOOKED UP YET.


##### notes

endpoint for general custom components...

```
# Component - A 'component' takes a request as input and returns html
@app.route("/component/<component>")
async def component(request, component):
    try:
        module = __import__(f'app.components.{component}')
        my_class = getattr(module, component.title())
        return response.html( str( my_class(request) ) )
    except Exception as e:
        print(e)
        return response.html( str( div("COMPONENT NOT FOUND!") ) )
```

or each div could have own endpoint / socket.

You don't necessarly need JSON or to parse anything because endpoints can return single divs or entire components using Domonic. This is really cool as you can visit an endpoint and see the html that it returns.

i.e visit the nav

http://localhost:8000/component/nav_menu?nav=default
http://localhost:8000/component/nav_menu?nav=pad


You can create custom endpoints to parse args manually incase you need to...

```
@app.route('/dir')
async def dir(request):
    return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )
```

pages can redraw element with javscript like so:

```
// pass an ElementID and an endpoint to redraw that div with the endpoints response
window.redraw = function( _id, endpoint ){
    $.get( endpoint, function( data ) { // TODO - q: can that go to a webworker?
    window.console.log(data)
      $( "#"+_id ).html( $(data).html() );
      // alert( "UPDATE was performed." );
    });
}
```

A component can be used to render within the original template.
Then called update on itself somethign like this...

```
button("TEST", _onclick=f"redraw('{self.id}', '/dir?directory={self.dir}/{name}&id={self.id}')")
```

A couple of global utils in .JS to redraw elements...

```
// create a new component and render it to the page
// add_to_page('/component?directory='+path+'&id=folder'+Math.round(Math.random()*999) );
window.add_to_page = function( endpoint ){
	$.get( endpoint, function( data ) {
			$('#page').append(data);
	});
}

// call this to get a new menu when app is in focus
window.redraw_menu = function( app ){
	$.get( '/component/nav_menu?nav='+app, function( data ) {
			$('#head').html($(data).html());
	});
}
```

<img src="https://github.com/byteface/Blueberry/blob/master/assets/img/fullscreen.png" alt="screenshot">