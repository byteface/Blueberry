from domonic.html import *
from domonic.terminal import pwd, ls, cat
from domonic.javascript import Global


class Markdown(object):

    def __init__(self, myfile='', _id: str = None):
        self.file = myfile
        if _id is None:
            self.id = "md" + str(hash(self.file))
        else:
            self.id = _id

    def get_file_content(self):
        if len(self.file) < 1:
            return ""
        return str(cat(self.file.rstrip('/')))

    def __str__(self):
        return str(
            div(
                script(_src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"),
                div(_id=self.id).html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a("close", _href="#", _class="destroy"),
                            a("minimize", _href="", _class="minimize"),
                            a("maximize", _href="#", _class="maximize")
                        ),
                        h1("Markdown Viewer", _class="titleInside"),
                        # div(_id=self.id, _name=self.id)
                        iframe(_id="FileFrame", _src="about:blank", _style="width:100%;height:100%;")
                    )
                ),
                # script(f'document.getElementById("{self.id}").innerHTML = marked(decodeURIComponent("{Global.encodeURIComponent(self.get_file_content())}"));')
                script(_type="text/javascript").html(
                    f'var doc = document.getElementById("FileFrame").contentWindow.document;\
                   doc.open();\
                   var result = marked(decodeURIComponent( "{Global.encodeURIComponent(self.get_file_content())}" ));\
                   doc.write( result );\
                   doc.close();\
                   ',
                '''
                $(".destroy").click(function(e) {
                    e.preventDefault();
                    $(this.hash).remove();
                });
                '''
                )
            )
        )
