import base64

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

# <!-- SFX -->
sfx = div(audio(_id="myAudio", _autoplay="true").html(
      source("Your browser does not support the audio element.", _src="assets/audio/blueberry.mp3", _type="audio/mp3")
    ),
    script(_type="text/javascript").html(
    '''    
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
    '''
))

# <!-- FAIL -->
fail = div(_id="fail").html(
        div(_class="fail-browser-logo").html(
            img(_src="assets/img/blueberry-logo-login.png", _alt="Mac OS X")
        ),
        div(_class="fail-browser").html(
            p(strong("Sorry your browser don't support CSS3!")) 
        )
    )


# <!-- BODY -->
bd = body( sfx, fail, 
    # <!-- BOOT -->
    div(_id="pageLoading").html(
        div(_class="loading").html(
            div(_class="blueberry-logo"),
            div(_class="spinner")
        )
    ),
    # <!-- LOGIN -->
    div(_id="pageLogin").html(
        header(_id="headlogin").html(
            nav(_id="menu-dx-login").html(
            ul(
                li(_class="wireless"),
                li(_class="time").html(
                    ul(li(_class="hours"),li(":",_class="point"),li(_class="min"))
                )
            )
        )
    ),
    div(_class="new-blueberry-logo"),
    div(_class="user-avatar").html(
        div(_id="avatar").html(
            a(_href="#hide", _class="hide", _id="hide"),
            a(_href="#show", _class="show", _id="show"),
            div(_id="cover"),
                div(img(_src="assets/img/avatar.png"), _class="ava-css"),
                div(p(whoami()), _class="logName" ),
                div(_id="switch").html(
                    div(_class="validate").html(
                        form(_action="#page").html(
                            input(_type="password", _id="password", _placeholder="Password"),
                            input(_type="submit", _class="submit"),
                            div(_class="tooltip-pass").html(
                                p("Password: admin")
                            )
                        )
                    )
                )
            )
        )
    ),

    # <!-- DESKTOP -->
    div(_id="page").html(

        nav_menu,

        div(_id="finder", _class="window finder ui-widget-content").html(
            nav(_class="control-window").html(
                a("close", _href="#finder", _class="close", **{"_data-rel":"close"}),
                a("minimize", _href="#", _class="minimize"),
                a("deactivate", _href="#", _class="deactivate")
            ),
            h1("About Peruser", _class="titleInside"),
            div(_class="container").html(
                div(_class="container-inside").html(
                    img(_src="assets/img/FinderIcon.png", _alt="Finder"),
                    div(_class="about-this").html(
                        h2("Peruser"),
                        p("The Desktop Experience"),
                        p("Peruser version 0.0.1", _class="small")
                    ),
                    div(_class="copyright").html(
                        p("© 2020 Eventual Technology"),
                        p("All Rights Reserved")
                    )
                )
            )
        ),

        div(_id="about-this-mac", _class="window mac").html(
            nav(_class="control-window").html(
                a("close", _href="#about-this-mac", _class="close", **{"_data-rel":"close"}),
                a("deactivate", _href="#", _class="deactivate"),
                a("deactivate", _href="#", _class="deactivate")
            ),
            h1("About This Box", _class="title-mac"),
            div(_class="container").html(
                div(_class="container-inside").html(
                    img(_src="assets/img/MacOSX.png", _alt="Mac OS X"),
                    div(_class="about-this").html(
                        p("Version 0.0.1"),
                        p(a("Software Update...", _class="button about", _href="#")),
                        ul(_class="hardware").html(
                            li(strong("Processor"), "2 Ghz Intel Core 2 Duo"),
                            li(strong("Memory"), "4 GB 1067 Mhz DDR3"),
                            li(strong("Startup Disk"), " Macintosh HD")
                        ),
                        p(a("More Info...", _class="button about", _href="#")),
                        div(_class="copyright").html(
                            p("© 2020 Eventual Technology"),
                            p("All Rights Reserved")
                        )
                    )
                )
            )
        ), 


        # div(_id="termy", _class="window termy").html(
        #     nav(_class="control-window").html(
        #         a("close", _href="#termy", _class="close", **{"_data-rel":"close"}),
        #         a("minimize", _href="#", _class="minimize"),
        #         a("maximize", _href="", _class="maximize"),
        #         div("maximize", _class="maximize")
        #     ),
        #     h1("Terminal", _class="titleInside"),
        #     iframe(_src="file:///Users/byteface/Desktop/peruse/terminal.html")
        # ),

        div(_id="warning", _class="window warning").html(
            div(_class="tab"),
            div(_class="container").html(
                div(_class="container-alert").html(
                    img(_src="assets/img/Alert.png", _alt="alert"),
                    div( _class="about-alert").html(
                        h2("Alert"),
                        p("This application cannot be used in this version"),
                        a("Close", _href="#warning", _class="button blink", **{"_data-rel":"close"} )
                    )
                )
            )
        ),

        div(_id="trash", _class="window warning").html(
            div(_class="tab"),
            div(_class="container").html(
                div(_class="container-alert").html(
                    img(_src="assets/img/FinderIcon.png", _width="48px", _height="48px", _alt="alert"),
                    div(_class="about-alert").html(
                        h2("Secure Empty Trash permanently erases the items in the Trash. Are you sure you want to permanently erase them?"),
                        p("If you choose Secure Empty Trash, you can't recover the items unless you've backed them up using Time Machine or another backup program."),
                        a("Secure Empty Trash", _href="#warning", _class="button blink", **{"_data-rel":""}),
                        a("Cancel", _href="#trash", _class="button simple", **{"_data-rel":"close"})
                    )
                )
            )
        ),

        Desktop('portfolio'),
        # peruser,
        # peruser2,
        Markdown('README.md'),
        Pad('portfolio/README.md'),
        context_menu,
        br(),br(),
        
        dock

    ), _id='body'
)


# render( html('<!DOCTYPE HTML>', hd, bd, _lang="en-US", _class="no-js"), 'blueberry.html' )
