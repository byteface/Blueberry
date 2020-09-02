from domonic.html import *

class Player(object):
    def __init__(self):
        self.name = "player"
        self.id = 'player'

    def __str__(self):
        return str(
            div(
                div(_id=self.id, _style="width:600px; height:400px;").html(
                    div(_id="share", _class="window share").html(
                        nav(_class="control-window").html(
                            a("close", _href="#"+self.id,
                              _class="destroy"),  # TODO - reinit
                            a("minimize", _href="deactivate", _class="minimize"),
                            a("maximize", _href="#", _class="maximize")
                        ),
                        h1("📺 Player", _class="titleInside"),
                        div(_id='content').html(
                            h2("media player test."),
                            br(),
                            button("Next >>", _id="skip_video"),
                            br(),
                            div(_id="video")
                        )
                    )
                ),
                script("""


                let videos = [
                  "https://www.youtube.com/watch?v=jOD1qvsD9vs",
                  "https://www.youtube.com/watch?v=kR6yGA-F16c",
                  "https://www.youtube.com/watch?v=59q-8_N4hL4",
                  "https://www.youtube.com/watch?v=PxD8-vxko64",
                  "https://www.youtube.com/watch?v=JKrP2Llwl-0",
                  "https://www.youtube.com/watch?v=ffpfm-YWP3o",
                  "https://www.youtube.com/watch?v=Qp5Io_nMiLY"
                ]
                $('#skip_video').on('click', function(){
                console.log('twat')
                  videos.unshift(videos.pop());
                  let vid = renderLink(videos[0]);
                  $('#video').html(vid);
                })

                const vid = renderLink(videos[0]);
                $('#video').html(vid);

                function renderLink( link ){

                  // window.console.log("--"+link+"--")
                  if( ( link === "" ) ||  ( link === null ) || ( link === undefined ) ){
                    return "";
                  }
                  var linky = link;

                  // VIMEO
                  if( linky.indexOf("vimeo.com") > -1 ){
                    var urlSplit = linky.split('/');
                    var vimId = urlSplit[urlSplit.length-1];
                    return '<div class="video-container"><iframe src="//player.vimeo.com/video/' + vimId + '" frameborder="0" width="100%" height="auto" allowfullscreen ></iframe></div><br>';
                  }

                  if( linky.indexOf("youtube.com") > -1 || linky.indexOf("youtu.be") > -1 ){
                    if( !(linky.indexOf("playlist") > -1) ) {
                      var myId = getYoutubeId(linky);
                      return '<div class="video-container"><iframe src="//www.youtube.com/embed/' + myId + '" frameborder="0" width="100%" height="auto;" allowfullscreen></iframe></div><br>';
                    }
                  }

                  function getYoutubeId(url) {
                      var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
                      var match = url.match(regExp);
                      if (match && match[2].length == 11) {
                          return match[2];
                      } else {
                          return 'NOT A VALID YOUTUBE URL';
                      }
                  }

                }
                    
                """)
            )
        )
