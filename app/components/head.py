from domonic.html import *

# <!-- HEAD -->
hd = head(
    meta(_content="text/html; charset=utf-8", **{"_http-equiv": "Content-Type"}),
    link(
        _rel="stylesheet",
        _type="text/css",
        _media="screen",
        _href="assets/css/style.css",
    ),
    link(
        _rel="stylesheet",
        _type="text/css",
        _media="screen",
        _href="assets/css/peruser.css",
    ),
    link(
        _rel="stylesheet",
        _type="text/css",
        _media="screen",
        _href="assets/css/jquery-ui.css",
    ),
    title("BlueBerry OS"),
    meta(
        _name="description",
        _content="BlueBerry OS - API based OS access built with web technologies",
    ),
    script(_type="text/javascript", _src="assets/js/modernizr.js"),
    script(_type="text/javascript", _src="assets/js/jquery-3.6.0.min.js"),
    script(_type="text/javascript", _src="assets/js/jquery-ui.min.js"),
    script(_type="text/javascript", _src="assets/js/master.js"),
)
