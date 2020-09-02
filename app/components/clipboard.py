from domonic.html import *
from domonic.javascript import Math
from domonic.terminal import ifconfig

class Clipboard(object):
    def __init__(self):
        self.name = "clipboard"
        self.id = 'clipboard'

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
                        h1("📋 Clipboard", _class="titleInside"),
                        div(_id='clipboard').html(
                            h2("test recordring users Clipboard data."),
                            # p('You can delete any items'),
                            div(_id="clip")
                        )
                    )
                ),
                script("""

                    if (navigator.clipboard 
                         && navigator.clipboard.read 
                         && navigator.clipboard.write) {
                        // setSupported(true);
                    } else {
                       // setSupported(false);
                    }

                    async function readClipboard(event) {
                       // event.preventDefault();
                       try {
                           const text = await navigator.clipboard.readText();  // writeText to do opposite
                           console.log('Pasted content: ', text);
                           $("#clip").html(text)
                       } catch (err) {
                          console.error('Failed to read clipboard contents: ', err);
                       }
                    }

                    $(document).ready(function() {
                        console.log('set!!')
                        setInterval( readClipboard, 3000 );
                    });

                    """)
            )
        )
