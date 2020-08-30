from domonic.html import *
from domonic.javascript import Math
from domonic.terminal import ifconfig


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
        return str(div(_id=self.id).html(
                div(_class="launcher_overlay", _style="width:100%; height:100%; \
                    position:absolute; \
                    top:0; \
                    left:0; \
                    background-color:black;").html(
                        "CONTENT"
            ),
            script('''
                $("#'''+self.id+'''").css('z-index', a++);

                $(".launcher_overlay").on( "click", function(){ $("#'''+self.id+'''").remove() } );

            ''')
            )
        )