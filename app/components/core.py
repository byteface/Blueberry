from domonic.html import *


class Window(object):

    def __init__(self, content, *args, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.content = content

    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:600px; height:400px; display:none;").html(
                    div(_class="window share").html( 
                        nav(_class="control-window").html(
                            # a("close", _href="#"+self.id, _class="destroy"), # TODO, required for components...
                            a("close", _href="#"+self.id, _class="close", **{"_data-rel":"close"}),
                            a("minimize", _href="#", _class="minimize"),
                            a("maximize", _href="#"+self.id, _class="maximize")
                            # a("deactivate", _href="#", _class="deactivate")
                        ),
                        h1(self.name, _class="titleInside"),
                        div(_id='content').html(
                          self.content
                        )
                    )
                ),
                script("""

                $(".destroy").click(function(e) {
                    e.preventDefault();
                    $(this.hash).remove();
                });

                """)
            )
        )


alert_tmpl = lambda title, msg: div(_id="trash", _class="window warning").html(
    div(_class="tab"),
    div(_class="container").html(
        div(_class="container-alert").html(
            img(_src="assets/img/FinderIcon.png", _width="48px", _height="48px", _alt="alert"),
            div(_class="about-alert").html(
                h2(title),
                h2(msg),
                a("Do it!", _href="#warning", _class="button blink", **{"_data-rel":""}),
                a("Cancel", _href="#trash", _class="button simple", **{"_data-rel":"close"})
            )
        )
    )
)

warning_tmpl = lambda msg: div(_id="warning", _class="window warning").html(
    div(_class="tab"),
    div(_class="container").html(
        div(_class="container-alert").html(
            img(_src="assets/img/Alert.png", _alt="alert"),
            div( _class="about-alert").html(
                h2("Alert"),
                p(msg),
                a("Close", _href="#warning", _class="button blink", **{"_data-rel":"close"} )
            )
        )
    )
)

iframe_tmpl = lambda content: div(_id="termy", _class="window termy").html(
    nav(_class="control-window").html(
        a("close", _href="#termy", _class="close", **{"_data-rel":"close"}),
        a("minimize", _href="#", _class="minimize"),
        a("maximize", _href="", _class="maximize"),
        div("maximize", _class="maximize")
    ),
    h1("Terminal", _class="titleInside"),
    iframe(_src=content)
)