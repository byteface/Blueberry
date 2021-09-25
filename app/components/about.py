import os
import sys

from domonic.html import *
from domonic.javascript import Math
from domonic.components import SpriteCSS

from .core import Window

VERSION = "0.0.3"

class About(Window):

    def __init__(self):

        anim = SpriteCSS('ken', 70, 80, 'assets/spritesheets/ken.png', 0.8, 4, True, 80)

        # if windows do something
        memory = None
        if sys.platform == 'win32':
            from domonic.cmd import Cmdcommand
            memory = Cmdcommand.run('wmic OS get FreePhysicalMemory /Value')
        else:
            from domonic.terminal import command
            memory = command.run("top -l 1 -s 0 | grep PhysMem")

        disk = None
        if sys.platform == 'win32':
            from domonic.cmd import Cmdcommand
            disk = Cmdcommand.run('wmic diskdrive get size')
        else:
            from domonic.terminal import command
            disk = command.run("df -h")

        
        self.content = div(_class="container").html(
                div(_class="container-inside").html(
                    # img(_src="assets/img/MacOSX.png", _alt="Mac OS X"),
                    anim,
                    div(_class="about").html(
                        p(f"Version {VERSION}"),
                        p(a("Software Update...", _class="button about", _href="#", _style="margin:10px;")),
                        ul(_class="hardware").html(
                            # li(strong("Processor"), ""),
                            li(strong("Memory :"), memory),
                            li(strong("Disk :"), disk)
                        ),
                        p(a("More Info...", _class="button about", _href="#", _style="margin:10px;")),
                        br(),
                        div(_class="copyright").html(
                            p("© 2020 Blueberry"),
                            sup("All Rights Reserved")
                        )
                    )
                )
            )

        Window.__init__(self, self.content, id="about", name="About this box")


class AboutPeruser(Window):

    def __init__(self):
 
        self.content = div(_class="container").html(
                div(_class="container-inside").html(
                    img(_src="assets/img/FinderIcon.png", _alt="Finder"),
                    div(_class="about-this").html(
                        h2("Peruser"),
                        p("The Desktop Experience"),
                        p(f"Peruser version {VERSION}", _class="small")
                    ),
                    div(_class="copyright").html(
                        p("© 2020 Blueberry"),
                        sup("All Rights Reserved")
                    )
                )
            )
        # )

        Window.__init__(self, self.content, id="about_peruser", name="About Peruser")
