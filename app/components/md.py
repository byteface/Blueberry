from domonic.html import *
from domonic.terminal import pwd, ls, cat
from domonic.javascript import Global


class Markdown(object):
    def __init__(self, myfile="", _id: str = None):
        self.file = myfile
        if _id is None:
            self.id = "md" + str(hash(self.file))
        else:
            self.id = _id

    def get_file_content(self):
        if len(self.file) < 1:
            return ""
        return str(cat(self.file.rstrip("/")))

    def __str__(self):
        return str(
            div(
                script(_src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"),
                div(_id=self.id).html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a("close", _href="#" + self.id, _class="destroy"),
                            a("minimize", _href="", _class="minimize"),
                            a("maximize", _href="#", _class="maximize"),
                        ),
                        h1("Markdown Viewer", _class="titleInside"),
                        # div(_id=self.id, _name=self.id)
                        iframe(
                            _id="FileFrame",
                            _src="about:blank",
                            _style="width:100%;height:100%;",
                        ),
                    )
                ),
                # script(f'document.getElementById("{self.id}").innerHTML = marked(decodeURIComponent("{Global.encodeURIComponent(self.get_file_content())}"));')
                script(_type="text/javascript").html(
                    f'var doc = document.getElementById("FileFrame").contentWindow.document;\
                   doc.open();\
                   var result = marked(decodeURIComponent( "{Global.encodeURIComponent(self.get_file_content())}" ));\
                   doc.write( result );\
                   doc.close();\
                   ',
                    """
                $(".destroy").click(function(e) {
                    e.preventDefault();
                    $(this.hash).remove();
                    redraw_menu('peruser')
                });
                """,
                ),
            )
        )


# - taking notes on breakdown to make a nav template for any app.
# - so that main nav can redraw to that app when switching context
md_nav_menu = nav(_id="menu").html(
    ul(
        li(
            a("🫐", _href="#all"),
            ul(_class="sublist").html(
                li(
                    a(
                        "About This Box",
                        _href="#about-this-mac",
                        **{"_data-rel": "show"},
                    )
                ),
                li("Software Updates..."),
                li("App Store..."),
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
        # -- BEFORE THIS STAYS SAME on any app
        # -- notes. to populate this NODE as a template we only need 'name' and list of links
        li(_class="here").html(
            a("Markdown Viewer", _href="#all"),
            ul(_class="sublist").html(
                li(a("About Markdown Viewer", _href="#md", **{"_data-rel": "show"})),
                li(_class="divider"),
                li("Preferences..."),
                li(_class="divider"),
                # li("Links",  # TODO - links to related services... i.e online .md file stuff
                #     span(_class="arrow"),
                #     ul(_class="sublist-menu").html(
                #         li("No Links Found", _class="disable"),
                #         li("http://www.whatever...")
                #     )
                # ),
                li(_class="divider"),
                li("Hide Markdown Viewer"),
                li("Hide Others"),
                li("Show All", _class="disable"),
                li("Quit Markdown Viewer"),
            ),
        ),
        li(
            a("File", _href="#all"),
            ul(_class="sublist").html(
                li("New", _class="disable"),
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
                li("Save", _class="disable"),
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
        # --- change depending on app
        li(
            a("Edit", _href="#all"),
            ul(_class="sublist").html(
                li("Copy", _class="disable"),
                li("Speech", span(_class="arrow")),
                li(_class="divider"),
                li("Emoji & Symbols"),
            ),
        ),
        # --- app custom menus...
        li(
            a("Options", _href="#all"),
            ul(_class="sublist").html(
                li(
                    "Some Option",
                    span(_class="arrow"),
                    ul(_class="sublist-menu").html(
                        li("nested option one"), li("nested option two")
                    ),
                ),
                li(_class="divider"),
                li("Open with..."),
                li("Validate with..."),
            ),
        ),
        # --- this may change depending on app
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
        # --- pretty much stays same below as well. just name changes in the Help section
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
                li("Markdown Viewer Help"),
            ),
        ),
    )
)
