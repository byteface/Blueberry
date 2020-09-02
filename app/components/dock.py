from domonic.html import *
from domonic.terminal import pwd, ls, cat


class Dock(object):

    def __init__(self, settings):
        self.id = "dock"
        self.settings = settings

    # def create_item(self, _id, link, label, alt, image):
    #     li(_id="expose").html(
    #         a(_href=settings['TWITTER'], _target="_blank").html(
    #             em(span("Twitter")),
    #             img(_src="assets/img/expose.png", _alt="Twitter")
    #         )
    #     ),


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
                        # a(_href="#warning", **{"_data-rel": "showOp"}).html(
                            div(_onclick="add_to_page('/component/launcher?&id=launcher')").html(
                                em(span("Apps")),
                                img(_src="assets/img/launchPad.png", _alt="Launchpad")
                            # )
                        )
                    ),


                    li(_id="expose").html(
                        a(_href=self.settings['TWITTER'], _target="_blank").html(
                            em(span("Twitter")),
                            img(_src="assets/img/expose.png", _alt="Twitter")
                        )
                    ) if self.settings['TWITTER'] else "",  # inline condition! cool!


                    li(_id="appStore").html(
                        a(_href=self.settings['GITHUB'], _target="_blank").html(
                            em(span("Github")),
                            img(_src="assets/img/appstore.png", _alt="Github")
                        )
                    ) if self.settings['GITHUB'] else "",  # inline ternary condition! cool!


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
                        a(_href=self.settings['LINKEDIN'], _target="_blank").html(
                            em(span("LinkedIn")),
                            img(_src="assets/img/address.png", _alt="LinkedIn")
                        )
                    ) if self.settings['LINKEDIN'] else "",  # inline ternary condition! cool!

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
                        # a(_href="", **{"_data-rel": "showOp"},
                        div(_onclick="add_to_page('/component?file=config.ini&id=config_pad')"
                        ).html(
                            em(span("Configuration")),
                            img(_src="assets/img/preferences.png",
                                _alt="preferences")
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
