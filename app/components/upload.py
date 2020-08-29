from domonic.html import *
from domonic.javascript import Math
from domonic.terminal import ifconfig

# TODO - class decorate the window rather than pasting each time
class Upload(object):
    '''
    Visit your IP from target machine, zip and upload ;)
    '''
    def __init__(self):
        self.name = "upload"
        self.id = 'upload' + str(Math.random()*9999)

    def get_ip(self):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:300px; height:400px;").html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a("close", _href="#"+self.id,
                              _class="destroy"),  # TODO - reinit
                            a("minimize", _href="deactivate", _class="minimize"),
                            a("maximize", _href="#", _class="maximize")
                        ),
                        h1("☝️ Upload File", _class="titleInside"),
                        div(_id='content').html(
                            h2("Send yourself a file ;)"),
                            form(_action="upload", _method="post", _enctype="multipart/form-data").html(
                                input(_type="file", _name="file"),
                                input(_type="submit", _value="Upload")
                            ),
                            p('A simple app to send yourself files.'),
                            p(f'Visit ur IP: {strong(self.get_ip())}:8000 from target machine, zip and upload ;)'),
                            br(),
                            h3("ifconfig dump..."),
                            div(str(br()).join(str(ifconfig()).split('\n')))
                        )
                    )
                )
            )
        )