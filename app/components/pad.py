from domonic.html import *
from domonic.terminal import pwd, ls, cat, whoami
from domonic.javascript import Global
from html import escape


class Pad(object):
    def __init__(self, myfile="", _id: str = None, *args, **kwargs):
        self.file = myfile
        if _id is None:
            self.id = "pad" + str(hash(self.file))
        else:
            self.id = _id

    def get_file_content(self):
        try:
            if len(self.file) < 1:
                return ""
            return str(cat(self.file.rstrip("/")))
        except Exception as e:
            print(e)
        return ""  # new files

    # def set_menu(): # TODO - update the menu
    # def save_file(self):
    # def new_document(self):

    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:300px; height:400px;").html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a(
                                "close", _href="#" + self.id, _class="destroy"
                            ),  # TODO - reinit
                            a("minimize", _href="deactivate", _class="minimize"),
                            a("maximize", _href="#", _class="maximize"),
                        ),
                        h1("📝 Pad", _class="titleInside"),
                        textarea(
                            self.get_file_content(),
                            _id=self.id,
                            _name=self.id,
                            _style="width:100%;height:100%;",
                        ),
                    )
                ),
                script(
                    """
                $(".destroy").click(function(e) {
                    e.preventDefault();
                    $(this.hash).remove();
                    redraw_menu('peruser')
                });
                //var a = 3;
                $('.content,.specific,.project,.share,.peruser').draggable({ handle: '.title-inside', start: function(event, ui) { $(this).css("z-index", a++); }});
                $(".window").draggable({ handle: '.titleInside, .title-mac, .tab, #toolbar, #view', refreshPositions: true, start: function(event, ui) { $(this).css("z-index", a++); } });
                
                $(".window").resizable({
                    handles: "n, e, s, w, ne, se, sw, nw"
                });

                $( "#"""
                    + self.id
                    + """" ).on( "dragstart", function( event, ui ) {
                    redraw_menu('pad')
                } );

                $(document).ready(function() {
                    $("#"""
                    + self.id
                    + """ .window").css('z-index', a++);
                });

            """
                ),
            )
        )


# pad = Pad()

pad_nav_menu = header(_id="head").html(
    nav(_id="menu").html(
        ul(
            li(  # _class="apple").html(
                a("🫐", _href="#all"),
                ul(_class="sublist").html(
                    li(
                        a(
                            "About This Box",
                            _href="#about-this-mac",
                            **{"_data-rel": "show"},
                        )
                    ),
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
                    li("Force Quit..."),
                    li(_class="divider"),
                    li("Sleep"),
                    li("Restart..."),
                    li("Shut Down..."),
                    li(_class="divider"),
                    li("Log Out..."),
                ),
            ),
            # -- BEFORE THIS SHOULD STAY SAME
            li(_class="here").html(
                a("Pad", _href="#all"),
                ul(_class="sublist").html(
                    li(a("About Pad", _href="#pad", **{"_data-rel": "show"})),
                    li(_class="divider"),
                    li("Preferences..."),
                    li(_class="divider"),
                    # li("Services",
                    #     span(_class="arrow"),
                    #     ul(_class="sublist-menu").html(
                    #         li("No Services Apply", _class="disable"),
                    #         li("Services Preferences...")
                    #     )
                    # ),
                    li(_class="divider"),
                    li("Hide Pad"),
                    li("Hide Others"),
                    li("Show All", _class="disable"),
                    li("Quit Pad"),
                ),
            ),
            li(
                a("File", _href="#all"),
                ul(_class="sublist").html(
                    # li(a("New Peruser Window", _href="#peruser", **{"_data-rel":"show"})),
                    li(
                        span(
                            "New",
                            _onclick=escape(
                                f"add_to_page('/component?file=newfile&id=pad_new')"
                            ),
                        )
                    ),  # todo randID and key from config
                    li("Open"),
                    li(
                        "Open Recent",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Somedoc.txt"),
                            li("Another.txt"),
                        ),
                    ),
                    li("Close"),
                    li("Save"),
                    li("Duplicate"),
                    li("Rename"),
                    li("Move To"),
                    li(
                        "Revert To",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Somedoc.txt"),
                            li("Another.txt"),
                        ),
                    ),
                    li("Export To PDF"),
                    li(_class="divider"),
                    li("Show Properties"),
                    li(_class="divider"),
                    li("Print"),
                    li("Page Setup"),
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
                    li(
                        "Find",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Find"),
                            li("Find & Replace"),
                            li("Find Next"),
                            li("Find Previous"),
                            li("Use Selection for Find"),
                            li("Select Line"),
                        ),
                    ),
                    li("Spelling and Grammar", span(_class="arrow")),
                    li("Substitutions", span(_class="arrow")),
                    li(
                        "Transformations",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Make Uppercase"), li("Make Lowercase"), li("Capitalise")
                        ),
                    ),
                    li("Speech", span(_class="arrow")),
                    li(_class="divider"),
                    li("Start Dictation"),
                    li("Emoji & Symbols"),
                ),
            ),
            li(
                a("Format", _href="#all"),
                ul(_class="sublist").html(
                    li(
                        "Font",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Show Fonts"),
                            li("Bold"),
                            li("Italic"),
                            li("Underline"),
                            li("Outline"),
                            li("Styles"),
                            li(_class="divider"),
                            li("Bigger"),
                            li("Smaller"),
                            li(_class="divider"),
                            li("Show Colors"),
                        ),
                    ),
                    li(
                        "Text",
                        span(_class="arrow"),
                        ul(_class="sublist-menu").html(
                            li("Align Left"),
                            li("Centre"),
                            li("Justify"),
                            li("Align Right"),
                            li(_class="divider"),
                            li(
                                "Writing Direction",
                                span(_class="arrow"),
                                ul(_class="sublist-menu").html(
                                    li("Align Left"),
                                    li("Centre"),
                                    li("Justify"),
                                    li("Align Right"),
                                ),
                            ),
                            li(_class="divider"),
                            li("Show Ruler"),
                            li("Copy Ruler"),
                            li("Paste Ruler"),
                            li(_class="divider"),
                            li("Spacing"),
                        ),
                    ),
                    li(_class="divider"),
                    li("Make Plain Text"),
                    li("Prevent Editing"),
                    li("Wrap to Page"),
                    li("Allow Hyphenation"),
                    li("Make Layout Vertical"),
                    li(_class="divider"),
                    li("List..."),
                    li("Table..."),
                ),
            ),
            li(
                a("View", _href="#all"),
                ul(_class="sublist").html(
                    li("Show Tab Bar"),
                    li("Show All Tabs"),
                    li("Dark Mode"),
                    li("Actual Size"),
                    li("Zoom In"),
                    li("Zoom Out"),
                    li(_class="divider"),
                    li("Go Fullscreen", _onclick="goFullScreen();"),
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
                    li("Some Document"),
                    li("Some Other Document"),
                ),
            ),
            li(
                a("Help", _href="#all"),
                ul(_class="sublist").html(
                    li(input(_placeholder="Search")),
                    li("Pad Help"),
                ),
            ),
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
            li(a(whoami(), _href="#all"), _class="username"),
            li("🔎"),
        )
    ),
)
