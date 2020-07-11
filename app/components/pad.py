# -*- coding: utf-8 -*-

import base64

# from domonic.javascript import Math
from domonic.html import *
from domonic.terminal import pwd, ls, cat

# <!-- PAD -->
class Pad(object):

    def __init__(self, myfile='', _id :str=None):
        self.file=myfile
        if _id is None:
            self.id = "pad"# + str(hash(self.file))
        else:
            self.id = _id

    def get_file_content(self) -> str :
        if len(self.file)<1 : return ""
        # print('get_file_contentget_file_contentget_file_contentget_file_contentget_file_contentget_file_content',self.file)
        return str(cat(self.file.rstrip('/')))
        return ""


    # @create
    # @read
    # @update
    # @delete
    # def do_somat - TODO - decorators as data providers?


    def __str__(self):
        return str(

          div(_id="pad").html(
            div(_id="share", _class="window share").html(
              nav(_class="control-window").html(
                a("close", _href="#", _class="close"),
                a("minimize", _href="deactivate", _class="minimize"),
                a("maximize", _href="#", _class="maximize")
              ),
                h1("Pad", _class="titleInside"),
                p(h1({self.get_file_content()}, _class="titleInside"))
            )
            )
            )

pad = Pad()