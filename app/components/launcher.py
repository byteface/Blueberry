from domonic.html import *
from domonic.javascript import Math
from domonic.javascript import Global
from domonic.terminal import ifconfig
from html import escape

class Launcher(object):
    '''
    Launch applications
     - TODO - only allow one instance of this

    - TODO - loop open sockets see what apps are running and display/link to them
    - something like this....
    sudo lsof -i -n -P | grep TCP | grep "LISTEN" | grep -v "127" 
    ... todo - test piping on domonic. dont think ive dont that yet.
    lsof('-i -n -P')

    '''
    def __init__(self, request, *args, **kwargs):
        self.name = "launcher"
        self.id = 'launcher'

    def __str__(self):

        b1 = button( "TEST LAUNCH PLAYER", _onclick="add_to_page('/component/player?id=player')" )
        b1.style.position = "absolute"
        b1.style.top = "100px"
        b1.style.left = "100px"

        b2 = button( "TEST LAUNCH UPLOADER", _onclick="add_to_page('/component/upload?id=upload')" )
        b2.style.position = "absolute"
        b2.style.top = "300px"
        b2.style.left = "100px"

        link1 = "/component/player?id=player"
        link2 = "/component/upload?id=upload"

        return str(div(_id=self.id).html(
                div(_class="launcher_overlay", _style="width:100%; height:100%; \
                    position:absolute; \
                    top:0; \
                    left:0; \
                    background-color:white;").html(
                        "CONTENT", b1, b2
            ),
            br(),br(),br(),br(),br(),br(),br(),br(),
            button( "TEST LAUNCH PLAYER", _onclick=escape(f"add_to_page({link1})") ),
            button( "TEST LAUNCH UPLOADER", _onclick=escape(f"add_to_page({link2})") ),
            script('''
                $("#'''+self.id+'''").css('z-index', a++);

                $(".launcher_overlay").on( "click", function(){ $("#'''+self.id+'''").remove() } );

            ''')
            )
        )