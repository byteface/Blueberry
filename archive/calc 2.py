# -*- coding: utf-8 -*-
from domonic.javascript import Math
from domonic.html import *


classless_css = link(_rel="stylesheet", _href="https://unpkg.com/marx-css/css/marx.min.css")
jquery = script(_src="https://code.jquery.com/jquery-3.5.1.min.js")

code = script('''
	function add(){
		$('#results').html( Number($('#a').val()) + Number($('#b').val()) )};
''')

calc = article(
  div( 
  	label('Add numbers:'), 
  	input(_id='a'), span('+'), input(_id='b'),  
  	button('Calculate', 
  		_id="calculate_button", 
  		_onclick="add();"),
  	div('Result:', div(_id="results"))
  )
)

render( html(head(classless_css, jquery, code), body(calc)), 'calc.html' )


# // TODO - serve

# from domonic.terminal import ls, touch
# import time
# ls( "| open .")
# touch( "1.hi")
# time.sleep(1)
# touch( "2.how")
# time.sleep(1)
# touch( "3.are")
# time.sleep(1)
# touch( "4.you")


from domonic.reply import Component

class Car(Component):

  def __init__(self, props):
    # super(props);
    self.state = { xPos: 1, yPos: 2, color: "red" } # if no datasource store on a session
    # TODO - bind to a data source.

  @reply('rest.update') # socket.onmessage
  def updateColor(self,col):
    self.setState({color:col}) #-> send state to server.

  # def js(self):
  # 	return str("""

  # 	""")

  # def css(self):
  # 	return str("""

  # 	""")

  # def style(self):
  # 	return str("""

  # 	""")

  def render(): # decorate with a UID
    return (
      div(
        h1(f'My {self.state.brand}')
        p(f'It is a {self.state.color} {self.state.model} from {self.state.year}.')
        button( "Change color", _type="button", _onclick=f'{self.updateColor("red")}' )
	)
    )


# _onclick=f'{self.updateColor('red')}'
# window.Domonic.Page.func('Car','updateColor')

# Car1.updateColor("red")

# Car1.updateColor( colorVar )


