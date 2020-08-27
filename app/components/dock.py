from domonic.html import *
from domonic.terminal import pwd, ls, cat


class Dock(object):

    def __init__(self):
        self.id = "dock"

    def __str__(self):
        return str(
            div(_class="dock").html(
                ul(
                    li(_id="finder").html(
                        a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            em(span("Peruser")),
                            img(_src="assets/img/FinderIcon.png", _alt="Finder")
                        )
                    ),
                    li(_id="launchPad").html(
                        a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            em(span("Launchpad")),
                            img(_src="assets/img/launchPad.png", _alt="Launchpad")
                        )
                    ),
                    li(_id="expose").html(
                        a(_href="https://twitter.com/byteface", _target="_blank").html(
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
                        a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            em(span("Safari")),
                            img(_src="assets/img/Safari.png", _alt="Safari")
                        )
                    ),
                    li(_id="iChat").html(
                        a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            em(span("CV")),
                            img(_src="assets/img/ichat.png", _alt="iChat")
                        )
                    ),
                    li(_id="addressBook").html(
                        a(_href="https://www.linkedin.com/in/byteface/", _target="_blank").html(
                            em(span("LinkedIn")),
                            img(_src="assets/img/address.png", _alt="LinkedIn")
                        )
                    ),
                    li(_id="preview").html(
                        a(_href="#termy", **{"_data-rel": "show"}).html(
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
                        a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            em(span("System Preferences")),
                            img(_src="assets/img/preferences.png",
                                _alt="System Preferences")
                        )
                    ),
                    li(_id="trash").html(
                        a(_href="#trash", **{"_data-rel": "showOpTrash"}).html(
                            em(span("Trash")),
                            img(_src="assets/img/trash.png", _alt="Trash")
                        )
                    )
                )
            )
        )

dock = Dock()
