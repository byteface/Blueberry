import base64

from domonic.html import *
from domonic.terminal import *


class Peruser(object):
    '''
    a file browser
    '''

    PROJECT_ROOT = lambda _id : f"redraw('{_id}', '/dir?directory='../'&id={_id}')"

    def __init__(self, mydir='.', _id :str=None):
        if "&&" in mydir: mydir='.'

        self.dir=mydir
        if _id is None:
            self.id = "peruser" + str(hash(self.dir))
        else:
            self.id = _id

    def create_folders(self) -> str :
        folders=[]
        for line in ls(f'-alp {self.dir}'):
            # if line == '.' or line == '../'): continue  # dont draw mac hidden dirs
            if '/' in line:
                folders.append(self.create_folder(line.split(' ')[-1]))
            else:
                folders.append(self.create_file(line.split(' ')[-1]))

        return ''.join([str(each) for each in folders])

    def create_folder(self, name: str ) -> str :
        el=div(_class='folder',
                _onclick=f"redraw('{self.id}', '/dir?directory={self.dir.rstrip('/')}/{name.lstrip('/')}&id={self.id}')"
            ).html(
            div(span('📁'), _style="font-size:70px;", _class='icon')
        )
        return el

    def create_file(self, name: str ):

        filepath = str(pwd()).strip('\n') + '/' + self.dir.rstrip('/') + '/' + name

        # el = str(h2('📄', span(name), _style="font-size: 40px;",
                # _onclick=f"redraw('pad', '/file?file={self.dir.rstrip('/')}/{name}/&id=pad')" ))

        # draw a file
        parts = name.split('.')
        docType = parts[1] if len(parts)>1 else ''
        filetype = docType  # txt,doc,xls,pdf
        if docType == "html":
            filetype = ''
        el = str(div(_class="file-type-icon",
            _onclick=f"redraw('pad', '/file?file={self.dir.rstrip('/')}/{name}/&id=pad')"
            ).html(
                span(_class="corner"),
                span(filetype, _class=f"type {filetype}")
        )),

        try:
            print('NAME:', name)
            
            images=['jpg','jpeg','png','gif']
            for image in images:
                if image in name:
                    print('THIS ONES AN IMAGE') # TODO - only take a render if its smaller than X
                    
                    # imgpath = "file:///" + str(pwd()).strip('\n') + '/' + self.dir.rstrip('/') + '/' + name
                    # el = img(_src=imgpath, _style="width:50px;height:50px;")

                    imgpath = str(pwd()).strip('\n') + '/' + self.dir.rstrip('/') + '/' + name
                    with open(imgpath, "rb") as img_file:
                        src = base64.b64encode(img_file.read()).decode('utf-8')

                    el = img(_src="data:image/png;base64,"+src, _style="width:50px;height:50px;", _class="imagefile",
                        **{'_data-target':'_blank'}, **{'_data-href':"data:image/png;base64, " + src} )

                    break

        except Exception as e:
            print('create file FAILED:', e)

        return el


    def create_list_view(self) -> str :
        files=[]
        for line in ls(f'-alp {self.dir}'):
            files.append(self.create_item(line.split(' ')[-1]))
        return str(''.join(files))

    def create_item(self, name: str ) -> str :
        if '/' in name:
            mytag = str(li('📁', span(name)))
        else:
            mytag = str(li('📄', span(name)))
            imgs=['jpg','jpeg','png','gif']
            for img in imgs:
                if img in name:
                    mytag = str(li('🖼️', span(name)))
                    break
        return str(mytag)

    def __str__(self):
        return str(
            div(_id=self.id, _class="window peruser").html(
                div(_class="test").html(
                    div(_id='toolbar').html(
                        nav(_class="control-window").html(
                            a("close", _href="#"+self.id, _class="destroy", **{"_data-rel":"destroy"}),
                            a("minimize", _href="#", _class="minimize"),
                            a("maximize", _href="#", _class="maximize")
                        ),
                        h1(f"{self.dir}", _class="titleInside", _id='windowname'),
                        div(_id='actions').html(
                            div(
                                button(span('🔙', _style="font-size:18px;"),
                                    _onclick=f"redraw('{self.id}', '/dir?directory={self.dir.rstrip('/')}/../&id={self.id}')"),
                                " ",
                                button(span('👉', 
                                    _style="font-size:18px;"))
                            )
                            # button("find", _id="find")
                        )
                    )
                ),

                div(_id='view').html(
                    div(_id='sidebar').html(
                        ul(
                            li(button("TEST", _onclick=Peruser.PROJECT_ROOT(self.id))),
                            li(span("Files", _class='group'),
                                ul( self.create_list_view() )  # <----------------
                            ),
                            # li(span("Bookmarks", _class='group'))
                        )
                    ),
                    div(_id='content').html( 
                        
                        self.create_folders()
                     )  # <----------------
                ),
        script('''

        $(".imagefile").hover(
          // Mouse Over
          function(){
            $(this).animate({width:60,height:60}, 100);
          },
          // Mouse Out
          function(){
              $(this).animate({width: 50,height: 50}, 100);
        });
        
        $(".imagefile").click(function () {
            var image = new Image();
            image.src = $(this).data("href");
            var w = window.open("");
            w.document.write(image.outerHTML);
        });

        var a = 3;
        $('.peruser').draggable({ handle: '.title-inside', start: function(event, ui) { $(this).css("z-index", a++); }});
        $(".window").draggable({ handle: '.titleInside, .title-mac, .tab, #toolbar, #view', refreshPositions: true, start: function(event, ui) { $(this).css("z-index", a++); } });
        $('.peruser').resizable({
        handles: "n, e, s, w"
        });

        $(".destroy").click(function(e) {
            e.preventDefault();
            $(this.hash).remove();
        });

        ''')
            )

        )

peruser = Peruser()
peruser2 = Peruser('assets')