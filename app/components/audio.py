from __future__ import unicode_literals
import youtube_dl

from domonic.html import *
from domonic.javascript import Math


class Audio(object):
    def __init__(self, request=None):
        self.name = "audio"
        self.id = "audio"  # + str(Math.random()*9999)

    def convert(self, inp, sam, chan, bit, out, format):
        """use ffmpeg to convert audi files"""

        # ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
        # -i - input file
        # -vn - Disable video
        # -ar - Set the audio sampling frequency.
        # -ac - Set the number of audio channels
        # -b:a - Converts the audio bitrate to be exact 192kbit per second
        ffmpeg(f"-i {inp} -vn -ar {sam} -ac {chan} -b:a {bit}k {outp}.{fmt}")

        # convert audio file
        return

    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:600px; height:400px;").html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a(
                                "close", _href="#" + self.id, _class="destroy"
                            ),  # TODO - reinit
                            a("minimize", _href="deactivate", _class="minimize"),
                            a("maximize", _href="#", _class="maximize"),
                        ),
                        h1("🎵 Audio Encoder", _class="titleInside"),
                        div(_id="content").html(
                            h2("ffmpeg test."),
                            label("Source:", _for="file"),
                            input(_type="file", _name="file"),
                            input(_type="browse", _value="Browse"),
                            button("🎧 Play Soundtrack", _id="play_audio"),
                            br(),
                            hr(),
                            h4("Audio Settings"),
                            label("Format:", _for="format"),
                            select(_name="format", _id="format").html(
                                option(".mp3", _value="mp3"),
                                option(".aiff", _value="aiff"),
                                option(".wav", _value="wav"),
                            ),
                            label("Bitrate:", _for="bitrate"),
                            select(_name="bitrate", _id="bitrate").html(
                                option("224", _value="224")
                            ),
                            label("Sampling Rate:", _for="sampling"),
                            select(_name="sampling", _id="sampling").html(
                                option("224", _value="224")
                            ),
                            label("Audio Channels:", _for="channels"),
                            select(_name="channels", _id="channels").html(
                                option("2", _value="2")
                            ),
                            label("Modify Speed:", _for="file"),
                            input(_type="speed", _name="speed"),
                            br(),
                            hr(),
                            label("Source:", _for="file"),
                            input(_type="file", _name="outp"),
                            input(_type="browse", _value="Browse"),
                            button("Begin Encoding", _id="enc_audio"),
                        ),
                    )
                ),
                script(
                    """
                const tunes = []
                """
                ),
            )
        )
