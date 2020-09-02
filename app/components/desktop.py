from domonic.html import *
from domonic.terminal import *
from domonic.javascript import Math

class Desktop(object):

    def __init__(self, dir='.'):
        self.dir = dir

    def create_folders(self) -> str :
        folders=[]
        for line in ls(f'-alp {self.dir}'):
            if '.' in line: continue  # skip hidden files
            if '/' in line:
                folders.append(self.create_folder(line.split(' ')[-1].strip('/')))
        return str(folders)

    def create_folder(self, name: str ) -> str :
        s = f'top:{Math.random()*100}px;left:{Math.random()*100}px;' 
        return str(
                div(_class='folder', _style=s,
                    **{"_data-path":self.dir+"/"+name}).html(
                    div(span('📁'), _style="font-size:70px;", _class='icon'),
                    span(name, _style="color: white;")
                )
                )

    def __str__(self, dif=''):
        return str(
            div(_style="top:200px;").html(
                div(_id='finder2').html(
                    div(_id='view').html(
                        self.create_folders()
                    )
                )
            ),
            )

# desktop = Desktop()
