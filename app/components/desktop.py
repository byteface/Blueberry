import os
import sys

from domonic.html import *
from domonic.terminal import *
from domonic.cmd import dir
from domonic.javascript import Math

class Desktop(object):

    def __init__(self, dir='.'):
        self.dir = dir
        self.count = 0

    def create_folders(self) -> str :
        folders=[]
        self.count = 0

        if sys.platform == 'win32':

            self.dir = os.getcwd()
            # self.dir = self.dir.replace('/', '\\')

            # for each fodler in the current directory add it to the list
            for f in dir(self.dir):
                if os.path.isdir(self.dir+"/"+f):
                    folders.append(self.create_folder(f))
                    self.count += 1
        else:

            for line in ls(f'-alp {self.dir}'):
                if '.' in line: continue  # skip hidden files
                if '/' in line:
                    folders.append(self.create_folder(line.split(' ')[-1].strip('/')))
                    self.count += 1

        # rewrite in python normally

        return str(folders)

    def create_folder(self, name: str ) -> str :
        # layout folders as columns
        xpos = 40+(Math.round(self.count/4))*100
        ypos = 60+(((self.count%3))*100)
        s = f'left:{xpos}px;top:{ypos}px;'
        # print(name, xpos, ypos)
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
