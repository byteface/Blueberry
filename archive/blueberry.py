# -*- coding: utf-8 -*-

# from domonic.javascript import Math
from domonic.html import *

# <!-- HEAD -->
hd = head(
    meta(_content="text/html; charset=utf-8", **{"_http-equiv":"Content-Type"}),
    link(_rel="stylesheet", _type="text/css", _media="screen", _href="assets/css/style.css"),
    link(_rel="stylesheet", _type="text/css", _media="screen", _href="assets/css/peruser.css"),
    title("BlueBerry OS"),
    meta(_name="description", _content="BlueBerry OS - API based OS access built with web technologies"),
    
    script(_type="text/javascript", _src="assets/js/modernizr.js"),
    script(_type="text/javascript", _src="http://code.jquery.com/jquery-1.7.1.min.js"),
    script(_type="text/javascript", _src="assets/js/jquery-ui-1.8.17.custom.min.js"),

    # script(_type="text/javascript", _src="assets/jquery-3.5.1.min.js"),
    # script(_type="text/javascript", _src="assets/js/jquery-ui.js"),
    # TODO - update breaks
    
    script(_type="text/javascript", _src="assets/js/master.js")
)

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
                div(p("Guest"), _class="logName" ),
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
        header(_id="head").html(
            nav(_id="menu").html(
                ul(
                    li(_class="apple").html(
                        a("Blueberry OS", _href="#all"),
                        ul(_class="sublist").html(
                            li(a("About This Box", _href="#about-this-mac", **{"_data-rel":"show"})),
                            li("Software Updates..."),
                            li("App Store..."),
                            li(_class="divider"),
                            li("System Preferences..."),
                            li("Dock",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("Turn Hiding Off"),
                                    li("Turn Magnification Off"),
                                    li(_class="divider"),
                                    li("Position on Left"),
                                    li("Position on Bottom"),
                                    li("Position on Right"),
                                    li(_class="divider"),
                                    li("Dock Preferences...")
                                )
                            ),
                            li(_class="divider"),
                            li("Recent Items",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("Applications", _class="disable", ),
                                    li(_class="divider"),
                                    li("Documents", _class="disable"),
                                    li(_class="divider"),
                                    li("Servers", _class="disable"),
                                    li(_class="divider"),
                                    li("Clear Menu")
                                )
                            ),
                            li(_class="divider"),
                            li("Force Quit..."),
                            li(_class="divider"),
                            li("Sleep"),
                            li("Restart..."),
                            li("Shut Down..."),
                            li(_class="divider"),
                            li("Log Out...")
                        )
                    ),
                    li(_class="here").html(
                        a("Peruser", _href="#all"),
                        ul(_class="sublist").html(
                            li(a("About Peruser", _href="#finder", **{"_data-rel":"show"})),
                            li(_class="divider"),
                            li("Preferences..."),
                            li(_class="divider"),
                            li("Secure Empty Trash..."),
                            li(_class="divider"),
                            li("Services",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("No Services Apply", _class="disable"),
                                    li("Services Preferences...")
                                )
                            ),
                            li(_class="divider"),
                            li("Hide Peruser"),
                            li("Hide Others"),
                            li("Show All", _class="disable")
                        )
                    ),
                    li(
                        a("File", _href="#all"),
                        ul(_class="sublist").html(
                            li(a("New Peruser Window", _href="#peruser", **{"_data-rel":"show"})),
                            li("New Folder"),
                            li("New Folder with Selection", _class="disable"),
                            li("New Smart Folder"),
                            li("New Burn Folder"),
                            li("Open", _class="disable"),
                            li("Open With", span(_class="arrow"), _class="disable"),
                            li("Print", _class="disable"),
                            li("Close Window", _class="disable"),
                            li(_class="divider"),
                            li("Get Info"),
                            li(_class="divider"),
                            li("Compress", _class="disable"),
                            li(_class="divider"),
                            li("Duplicate", _class="disable"),
                            li("Make Alias", _class="disable"),
                            li("Quick Look", _class="disable"),
                            li("Show Original", _class="disable"),
                            li("Add to Sidebar", _class="disable"),
                            li(_class="divider"),
                            li("Move to Trash", _class="disable"),
                            li("Eject", _class="disable"),
                            li("Burn Desktop to Disc..."),
                            li(_class="divider"),
                            li("Find"),
                            li(_class="divider"),
                            li("Label:", _class="disable")
                        ) 
                    ),
                    li(
                        a("Edit", _href="#all"),
                        ul(_class="sublist").html(
                            li("Undo", _class="disable"),
                            li("Redo", _class="disable"),
                            li(_class="divider"),
                            li("Cut", _class="disable"),
                            li("Copy", _class="disable"),
                            li("Paste", _class="disable"),
                            li("Select All"),
                            li(_class="divider"),
                            li("Show Clipboard"),
                            li(_class="divider"),
                            li("Special Characters...")
                        )
                    ),
                    li(
                        a("View", _href="#all"),
                        ul(_class="sublist").html(
                            li("as Icons", _class="disable"),
                            li("as List", _class="disable"),
                            li("as Columns", _class="disable"),
                            li("as Cover Flow", _class="disable"),
                            li(_class="divider"),
                            li("Clean Up"),
                            li("Clean Up By",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("Name"),
                                    li("Kind"),
                                    li("Date Modified"),
                                    li("Date Created"),
                                    li("Size"),
                                    li("Label")
                                )
                            ),
                            li("Sort By",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li(None),
                                    li(_class="divider"),
                                    li("Snap to Grid"),
                                    li(_class="divider"),
                                    li("Name"),
                                    li("Kind"),
                                    li("Date Last Opened"),
                                    li("Date Added"),
                                    li("Date Modified"),
                                    li("Date Created"),
                                    li("Size"),
                                    li("Label"),
                                )
                            ),
                            li(_class="divider"),
                            li("Hide Path Bar", _class="disable"),
                            li("Hide Status Bar", _class="disable"),
                            li("Hide Sidebar", _class="disable"),
                            li(_class="divider"),
                            li("Toolbar", _class="disable"),
                            li("Customize Toolbar...", _class="disable"),
                            li(_class="divider"),
                            li("Show View Options...")
                        ),    
                    ),
                    li(
                        a("Go", _href="#all"),
                        ul(_class="sublist").html(
                            li("Back", _class="disable"),
                            li("Forward", _class="disable"),
                            li("Enclosing Folder"),
                            li(_class="divider"),
                            li("All My Files"),
                            li("Documents"),
                            li("Desktop"),
                            li("Downloads"),
                            li("Home"),
                            li("Computer"),
                            li("AirDrop"),
                            li("Network"),
                            li("Applications"),
                            li("Utilities"),
                            li(_class="divider"),
                            li("Recent Folders",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("2012-01-10"),
                                    li("Archieves"),
                                    li("buildFiles"),
                                    li("MyProjects"),
                                    li("XCode_iPhone"),
                                    li(_class="divider"),
                                    li("Clear Menu")
                                )
                            ),
                            li(_class="divider"),
                            li("Go to Folder..."),
                            li("Connect to Server...")
                        )    
                    ),
                    li(
                        a("Window", _href="#all"),
                        ul(_class="sublist").html(
                            li("Minimize", _class="disable"),
                            li("Zoom", _class="disable"),
                            li("Cycle Through Windows", _class="disable"),
                            li(_class="divider"),
                            li("Bring All to Front")
                        )   
                    ),
                    li(a("Help", _href="#all"))
                )
            ),
            nav(_id="menu-dx").html(
                ul(
                    li(a("Wireless", _href="#all"), _class="wireless"),
                    li(_class="time").html(
                        ul(
                            li(_id="DateAbbr"),
                            li(_class="hour"),
                            li(":", _class="point"),
                            li(_class="mins")
                        )
                    ),
                    li(a("Guest", _href="#all"), _class="username")
                )
            ),

            div(_id="finder", _class="window finder").html(
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
                               p("TM and © 2020 Eventual Technology"),
                               p("All Rights Reserved")
                            )
                        )
                    )
                )
            ), 


            div(_id="termy", _class="window termy").html(
                nav(_class="control-window").html(
                    a("close", _href="#termy", _class="close", **{"_data-rel":"close"}),
                    a("minimize", _href="#", _class="minimize"),
                    a("deactivate", _href="#", _class="deactivate")
                ),
                h1("Terminal", _class="titleInside"),
                iframe(_src="file:///Users/byteface/Desktop/peruse/terminal.html")
            ),


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


            # <nav class="control-window">
            # a(_href="#", _class="deactivate">deactivate)
            # a(_href="#", _class="deactivate">deactivate)
            # a(_href="#", _class="deactivate">deactivate)
            # )

            # div(_id="share", _class="window share",
            #   nav(_class="control-window",
            #      a("close", _href="#", _class="close"),
            #        a("minimize", _href="#", _class="minimize"),
            #        a("maximize", _href="#", _class="maximize")
            #     )
            #     h1("Share This", _class="titleInside")
            # )


            div(_id="peruser", _class="window peruser").html(

                div(_id='finder2').html(
                    div(_id='toolbar').html(
                        nav(_class="control-window").html(
                            a("close", _href="#peruser", _class="close", **{"_data-rel":"close"}),
                            a("minimize", _href="#", _class="minimize"),
                            a("deactivate", _href="#", _class="deactivate")
                        ),
                        div(i(), "All My Files", _id='windowname'),
                        div(_id='actions').html(
                            div(_id='back'),
                            div(_id='next'),
                            div(_id='iconV'),
                            div(_id='list'),
                            div(_id='grid'),
                            div(i(_class='view'), _id='coverflow' ),
                            div(_id='settings'),
                            div(_id='share'),
                            input(_results='0', _type='search')
                        )
                    )
                ),

                div(_id='view').html(
                    div(_id='sidebar').html(
                        ul(
                            li(
                                span("Favorites", _class='group'),
                                ul(
                                    li(i(_class='afiles'), "All My Files", _class='current_page'),
                                    li(i(_class='airdrop'), "AirDrop"),
                                    li(i(_class='apps'), "Applications"),
                                    li(i(_class='desk'), "Desktop"),
                                    li(i(_class='docs'), "Documents"),
                                    li(i(_class='downs'), "Downloads"),
                                    li(i(_class='mov'), "Movies"),
                                    li(i(_class='music'), "Music"),
                                    li(i(_class='pic'), "Pictures")
                                )
                            ),
                            li(span("Shared", _class='group'))
                        )
                    ),
                    div(_id='content').html(
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Desktop")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Documents")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Downloads")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Movies")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Music")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Pictures")
                        ),
                        div(_class='folder').html(
                            div(_class='icon'),
                            span("Public")
                        )
                    )
                )
            )
        ),



        br(),br(),
        # <!-- DESKTOP FOLDERS -->
        div(
            div(_id='finder2').html(
                div(_id='view').html(

                    # blueberry.Folder('Projects'),
                    # blueberry.Folder('RnD'),
                    # blueberry.Folder('Random')

                    div(_class='folder').html(
                        div(_class='icon'),
                        span("Projects", _style="color: white;")
                    ),
                    div(_class='folder').html(
                        div(_class='icon'),
                        span("RnD", _style="color: white;")
                    ),
                    div(_class='folder').html(
                        div(_class='icon'),
                        span("Random", _style="color: white;")
                    )
                )
            )
        ),


        # <!-- DOCK -->
        div(_class="dock").html(
            ul(
                li(_id="finder").html(
                    a(_href="#warning", **{"_data-rel":"showOp"}).html(
                        em(span("Peruser")),
                        img(_src="assets/img/FinderIcon.png", _alt="Finder")
                    )
                ),
                li(_id="launchPad").html(
                    a(_href="#warning", **{"_data-rel":"showOp"}).html(
                        em(span("Launchpad")),
                        img(_src="assets/img/launchPad.png", _alt="Launchpad")
                    )
                ),
                li(_id="expose").html(
                    a(_href="https://twitter.com/eventualtechno1", _target="_blank").html(
                        em(span("Twitter")),
                        img(_src="assets/img/expose.png", _alt="Twitter")
                    )
                ),
                li(_id="appStore").html(
                    a(_href="https://github.com/byteface", _target="_blank").html(
                        em(span("Github")),
                        img(_src="assets/img/appstore.png", _alt="Github")
                    )
                ),
                li(_id="safari").html(
                    a(_href="#warning", **{"_data-rel":"showOp"}).html(
                        em(span("Safari")),
                        img(_src="assets/img/Safari.png", _alt="Safari")
                    )
                ),
                li(_id="iChat").html(
                    a(_href="#warning", **{"_data-rel":"showOp"}).html(
                        em(span("CV")),
                        img(_src="assets/img/ichat.png", _alt="iChat")
                    )
                ),
                # li(_id="facetime").html(
                #     a(_href="#warning", **{"_data-rel":"showOp"}).html(
                #         em(span("FaceTime")),
                #         img(_src="assets/img/facetime.png", _alt="Facetime")
                #     )
                # ),
                li(_id="addressBook").html(
                    a(_href="https://www.linkedin.com/in/byteface/", _target="_blank").html(
                        em(span("LinkedIn")),
                        img(_src="assets/img/address.png", _alt="LinkedIn")
                    )
                ),
                li(_id="preview").html(
                    a(_href="#termy", **{"_data-rel":"show"}).html(
                        em(span("Terminal")),
                        img(_src="assets/img/preview.png", _alt="Preview")
                    )
                ),
                li(_id="iTunes").html(
                    a(_href="https://open.spotify.com/").html(
                        em(span("Spotify")),
                        img(_src="assets/img/iTunes.png", _alt="iTunes")
                    )
                ),
                li(_id="preferences").html(
                    a(_href="#warning", **{"_data-rel":"showOp"}).html(
                        em(span("System Preferences")),
                        img(_src="assets/img/preferences.png", _alt="System Preferences")
                    )
                ),
                li(_id="trash").html(
                    a(_href="#trash", **{"_data-rel":"showOpTrash"}).html(
                        em(span("Trash")),
                        img(_src="assets/img/trash.png", _alt="Trash")
                    )
                )
            )
        )
    )
)


render( html('<!DOCTYPE HTML>', hd, bd, _lang="en-US", _class="no-js"), 'blueberry.html' )
