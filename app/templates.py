import base64
import configparser

# from domonic.javascript import Math
from domonic.html import *
from domonic.terminal import pwd, whoami

from .components.context_menu import *
from .components.pad import *
from .components.md import *
from .components.dock import *
from .components.head import *
from .components.desktop import *
from .components.peruser import *
from .components.nav_menu import *
from .components.upload import *
from .components.launcher import *

# from .components.clipboard import *
from .components.player import *
from .components.audio import *
from .components.about import *
from .components.core import *

# to customise update the config.ini file
config = configparser.ConfigParser()
config.read("config.ini")
profile = "default"

app_settings = {}
app_settings["DESKTOP"] = config.get(profile, "DESKTOP", fallback=".")
app_settings["IS_ROOT"] = config.get(profile, "IS_ROOT", fallback=True)
app_settings["UPLOAD_DIR"] = config.get(profile, "UPLOAD_DIR", fallback="./Uploads")
# app.config['WALLPAPER'] = config.get(profile,'WALLPAPER', fallback='')
# dock --
dock_settings = {}
dock_settings["TWITTER"] = config.get(profile, "TWITTER", fallback="")
dock_settings["GITHUB"] = config.get(profile, "GITHUB", fallback="")
dock_settings["WEBSITE"] = config.get(profile, "WEBSITE", fallback="")
dock_settings["CV"] = config.get(profile, "CV", fallback="")
dock_settings["LINKEDIN"] = config.get(profile, "LINKEDIN", fallback="")
dock_settings["SPOTIFY"] = config.get(profile, "SPOTIFY", fallback="")
dock = Dock(dock_settings)


# <!-- SFX -->
sfx = div(
    audio(_id="myAudio", _autoplay="true").html(
        source(
            "Your browser does not support the audio element.",
            _src="assets/audio/blueberry.mp3",
            _type="audio/mp3",
        )
    ),
    script(_type="text/javascript").html(
        """    
    $( document ).ready(function() {
       
        $( '.blueberry-logo' ).on('click', function() {
            let sound = document.getElementById("myAudio");
            sound.currentTime = 0;
            sound.play();

            goFullScreen();
        });

        $( '.maximize' ).on('click', function() {
            goFullScreen();
        });

    });
    """
    ),
)

# <!-- FAIL -->
fail = div(_id="fail").html(
    div(_class="fail-browser-logo").html(
        img(_src="assets/img/blueberry-logo-login.png", _alt="Mac OS X")
    ),
    div(_class="fail-browser").html(
        p(strong("Sorry your browser don't support CSS3!"))
    ),
)


# <!-- BODY -->
bd = body(
    sfx,
    fail,
    # <!-- BOOT -->
    div(_id="pageLoading").html(
        div(_class="loading").html(div(_class="blueberry-logo"), div(_class="spinner"))
    ),
    # <!-- LOGIN -->
    div(_id="pageLogin").html(
        header(_id="headlogin").html(
            nav(_id="menu-dx-login").html(
                ul(
                    li(_class="wireless"),
                    li(_class="time").html(
                        ul(
                            li(_class="hours"),
                            li(":", _class="point"),
                            li(_class="min"),
                        )
                    ),
                )
            )
        ),
        div(_class="new-blueberry-logo"),
        div(_class="user-avatar").html(
            div(_id="avatar").html(
                # a(_href="#hide", _class="hide", _id="hide"),
                # a(_href="#show", _class="show", _id="show"),
                div(_id="cover"),
                div(img(_src="assets/img/avatar2.jpg"), _class="ava-css"),
                div(p(whoami()), _class="logName"),
                div(_id="switch").html(
                    div(_class="validate").html(
                        form(_action="#page").html(
                            input(
                                _type="password",
                                _id="password",
                                _placeholder="Password",
                            ),
                            input(_value="►", _type="submit", _class="submit"),
                            div(_class="tooltip-pass").html(p("Password: admin")),
                        )
                    )
                ),
            )
        ),
    ),
    # <!-- DESKTOP -->
    div(_id="page").html(
        nav_menu,
        # hidden windows
        AboutPeruser(),
        About(),
        # loading iframes inside windows
        # iframe_tmpl("/static/terminal.html"),
        # -- alerts
        warning_tmpl("This application cannot be used in this version"),
        alert_tmpl(
            "Trash", "Warning: Items moved to trash are PERMANENTLY ERASED FOREVER!"
        ),
        # init folders for the desktop
        # print(  "gawsh", app_settings['DESKTOP'] ),
        Desktop(app_settings["DESKTOP"]),
        # -- apps
        # Upload(),
        # Clipboard(),
        # Audio(),
        # Player(),
        # Markdown('README.md'),
        # Pad('desktop/README.md'),
        # -- other
        # context_menu,
        br(),
        br(),
        dock,
    ),
)
