from domonic.html import *
from domonic.terminal import pwd, ls, cat
from domonic.javascript import Global


class Pad(object):

    def __init__(self, myfile='', _id: str = None):
        self.file = myfile
        if _id is None:
            self.id = "pad" + str(hash(self.file))
        else:
            self.id = _id

    def get_file_content(self):
        if len(self.file) < 1:
            return ""
        return str(cat(self.file.rstrip('/')))

    # def set_menu(): # TODO - update the menu
    # def save_file(self):
    # def new_document(self):

    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:300px; heigh:400px;").html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a("close", _href="#"+self.id, _class="destroy"),  # TODO - reinit
                            a("minimize", _href="deactivate", _class="minimize"),
                            a("maximize", _href="#", _class="maximize")
                        ),
                        h1("📝 Pad", _class="titleInside"),
                        textarea(self.get_file_content(), _id=self.id,
                                 _name=self.id, _style="width:100%;height:100%;")
                    )
                ),            script('''
            $(".destroy").click(function(e) {
                e.preventDefault();
                $(this.hash).remove();
            });


var a = 3;
$('.content,.specific,.project,.share,.peruser').draggable({ handle: '.title-inside', start: function(event, ui) { $(this).css("z-index", a++); }});
$(".window").draggable({ handle: '.titleInside, .title-mac, .tab, #toolbar, #view', refreshPositions: true, start: function(event, ui) { $(this).css("z-index", a++); } });

            
            ''')
            )
        )

# pad = Pad()
