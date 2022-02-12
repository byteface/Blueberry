from domonic.html import *
from domonic.terminal import whoami
from html import escape


class Nav_Menu(object):
    def __init__(self, request, *args, **kwargs):
        self.id = "menu"
        self.menu = nav_menu
        # print(request.args['nav'])
        try:
            if request.args["nav"][0] == "pad":
                from app.components.pad import pad_nav_menu

                self.menu = pad_nav_menu
        except Exception as e:
            print(e)

    def __str__(self):
        return str(self.menu)


username = whoami()

nav_menu = header(_id="head").html(
    nav(_id="menu").html(
        ul(
            li(  # _class="apple").html(
                a("🫐", _href="#all"),
                ul(_class="sublist").html(
                    li(a("About This Box", _href="#about", **{"_data-rel": "show"})),
                    li(
                        a(
                            "Software Updates...",
                            _href="https://github.com/byteface/Blueberry",
                        )
                    ),
                    li(
                        a("App Store...", _href="https://github.com/byteface/Blueberry")
                    ),
                    li(_class="divider"),
                    li("System Preferences..."),
                    li(
                        "Dock",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Turn Hiding Off"),
                            li("Turn Magnification Off"),
                            li(_class="divider"),
                            li("Position on Left"),
                            li("Position on Bottom"),
                            li("Position on Right"),
                            li(_class="divider"),
                            li("Dock Preferences..."),
                        ),
                    ),
                    li(_class="divider"),
                    li(
                        "Recent Items",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Applications", _class="disable"),
                            li(_class="divider"),
                            li("Documents", _class="disable"),
                            li(_class="divider"),
                            li("Servers", _class="disable"),
                            li(_class="divider"),
                            li("Clear Menu"),
                        ),
                    ),
                    li(_class="divider"),
                    li("Force Quit...", _onclick=""),
                    li(_class="divider"),
                    li("Sleep"),
                    li("Restart..."),
                    li("Shut Down..."),
                    li(_class="divider"),
                    li("Log Out...", _onclick="window.location=''"),
                ),
            ),
            li(_class="here").html(
                a("Peruser", _href="#all"),
                ul(_class="sublist").html(
                    li(
                        a(
                            "About Peruser",
                            _href="#about_peruser",
                            **{"_data-rel": "show"},
                        )
                    ),
                    li(_class="divider"),
                    li("Preferences..."),
                    li(_class="divider"),
                    li("Secure Empty Trash..."),
                    li(_class="divider"),
                    li(
                        "Services",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("No Services Apply", _class="disable"),
                            li("Services Preferences..."),
                        ),
                    ),
                    li(_class="divider"),
                    li("Hide Peruser"),
                    li("Hide Others"),
                    li("Show All", _class="disable"),
                ),
            ),
            li(
                a("File", _href="#all"),
                ul(_class="sublist").html(
                    # li(a("New Peruser Window", _href="#peruser", **{"_data-rel":"show"})),
                    li(
                        span(
                            "New Peruser Window",
                            _onclick=escape(
                                f"add_to_page('/dir?directory=static/desktop&id=peruser_new')"
                            ),
                        )
                    ),  # todo randID and key from config
                    li("New Folder"),
                    li("New Folder with Selection", _class="disable"),
                    # li("New Smart Folder"),
                    # li("New Burn Folder"),
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
                    # li("Show Original", _class="disable"),
                    li("Add to Sidebar", _class="disable"),
                    li(_class="divider"),
                    li("Move to Trash", _class="disable"),
                    # li("Eject", _class="disable"),
                    # li("Burn Desktop to Disc..."),
                    li(_class="divider"),
                    li("Find"),
                    li(_class="divider"),
                    li("Label:", _class="disable"),
                ),
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
                    li("Special Characters..."),
                ),
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
                    li(
                        "Clean Up By",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Name"),
                            li("Kind"),
                            li("Date Modified"),
                            li("Date Created"),
                            li("Size"),
                            li("Label"),
                        ),
                    ),
                    li(
                        "Sort By",
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
                        ),
                    ),
                    li(_class="divider"),
                    li("Hide Path Bar", _class="disable"),
                    li("Hide Status Bar", _class="disable"),
                    li("Hide Sidebar", _class="disable"),
                    li(_class="divider"),
                    li("Toolbar", _class="disable"),
                    li("Customize Toolbar...", _class="disable"),
                    li(_class="divider"),
                    li("Show View Options..."),
                    li("Go Fullscreen", _onclick="goFullScreen();"),
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
                    li(
                        "Desktop",
                        _onclick=escape(
                            f"add_to_page('/dir?directory=static/desktop&id=peruser_desktop')"
                        ),
                    ),
                    li(
                        "Uploads",
                        _onclick=escape(
                            f"add_to_page('/dir?directory=uploads&id=peruser_uploads')"
                        ),
                    ),
                    li("Home"),
                    li("Computer"),
                    # li("AirDrop"),
                    # li("Network"),
                    li("Applications"),
                    li("Utilities"),
                    li(_class="divider"),
                    li(
                        "Recent Folders",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("2019"), li(_class="divider"), li("Clear Menu")
                        ),
                    ),
                    li(_class="divider"),
                    li("Go to Folder..."),
                    li("Connect to Server..."),
                ),
            ),
            li(
                a("Window", _href="#all"),
                ul(_class="sublist").html(
                    li("Minimize", _class="disable"),
                    li("Zoom", _class="disable"),
                    li("Cycle Through Windows", _class="disable"),
                    li(_class="divider"),
                    li("Bring All to Front"),
                ),
            ),
            li(a("Help", _href="#all")),
        )
    ),
    nav(_id="menu-dx").html(
        ul(
            li("📶"),
            li(_class="time").html(
                ul(
                    li(_id="DateAbbr"),
                    li(_class="hour"),
                    li(":", _class="point"),
                    li(_class="mins"),
                )
            ),
            li(a(username, _href="#all"), _class="username"),
            li("🔎"),
        )
    ),
)
