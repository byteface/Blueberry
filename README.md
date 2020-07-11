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

hacking/mucking around... just testing how templates might be rendered from components. Cool that each div could have own endpoint or socket. Looks a bit like react backwards, in python.


I can create endpoints to return single divs or components...
```
@app.route('/dir')
async def dir(request):
    return response.html( str(Peruser(request.args['directory'][0], request.args['id'][0])) )
```

the page redraws the element with javscript like so:

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

The same component was used to render the original template.

And called update on itself like this...

```
button("TEST", _onclick=f"redraw('{self.id}', '/dir?directory={self.dir.rstrip('/')}/{name.lstrip('/')}&id={self.id}')")
```


<img src="https://github.com/byteface/Blueberry/blob/master/assets/img/fulllscreen.png" alt="screenshot">