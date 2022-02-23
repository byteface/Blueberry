<h1 align="center">
    <img src="https://github.com/byteface/Blueberry/blob/master/assets/img/pie.jpg"
    style="background-color:rgba(0,0,0,0);" height=230 alt="Blueberry: browser based OS">
    <br>
    Blueberry π
    <br>
    <sup><sub><sup>A browser based OS built using domonic</sup></sub></sup>
    <br>
</h1>

# Blueberry π

##### setup

```bash
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
```

##### running

```bash
python3 blueberry.py
```

##### customising

edit the congi.ini

comment out the things you don't want to appear in the Dock

not all settings working yet

#### nav

The site useses hotwiring concepts where htmls components endpoints. i.e. renders html...

- http://localhost:8000/component/nav_menu?nav=default
- http://localhost:8000/component/nav_menu?nav=pad

#### upgrade

If you've had Blueberry before just completely delete it and reinstall. The domonic lib changes a lot atm.

<img src="https://github.com/byteface/Blueberry/blob/master/assets/img/fullscreen.png" alt="screenshot">

