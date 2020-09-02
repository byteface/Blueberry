// if (location.hash) {
// 	setTimeout(function() {
// 		window.scrollTo(0, 0);
// 	}, 1);
// }

var a = 3; // layers - GLOBAL ZINDEX tracker


function goFullScreen(){
	var elem = document.getElementById("body");
	
	  if (elem.requestFullscreen) {
		elem.requestFullscreen();
	  } else if (elem.mozRequestFullScreen) { /* Firefox */
		elem.mozRequestFullScreen();
	  } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
		elem.webkitRequestFullscreen();
	  } else if (elem.msRequestFullscreen) { /* IE/Edge */
		elem.msRequestFullscreen();
	  }
}

// pass an ElementID and an endpoint to redraw that div with the endpoints response
window.redraw = function( _id, endpoint ){
	$.get( endpoint, function( data ) {
	// window.console.log(data)
	  $( "#"+_id ).html( $(data).html() );
	  // alert( "UPDATE was performed." );
	});
}

// create a new component and render it to the page
// add_to_page('/component?directory='+path+'&id=folder'+Math.round(Math.random()*999) );
window.add_to_page = function( endpoint ){

	console.log('add_to_page:')
	console.log(endpoint)
	$.get( endpoint, function( data ) {
		$('#page').append(data);
	});
}

// call this to get a new menu when app is in focus
window.redraw_menu = function( app ){
	$.get( '/component/nav_menu?nav='+app, function( data ) {
			$('#head').html($(data).html());
	});
}



$(document).ready(function() {
//-----------------------------------------------------------------------------------
//	0.	Modernizr test
//-----------------------------------------------------------------------------------
if (Modernizr.cssanimations) {
	$('#fail').remove();
}
else {
	$('#fail').addClass('visible');
}

//-----------------------------------------------------------------------------------
//	1.	Clock
//-----------------------------------------------------------------------------------

var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]; 
var dayNames= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

var newDate = new Date();
newDate.setDate(newDate.getDate());
$('#DateAbbr').html(dayNames[newDate.getDay()].substr(0,3) + " ");

setInterval( function() {
	var minutes = new Date().getMinutes();
	$(".min, .mins").html(( minutes < 10 ? "0" : "" ) + minutes);
    },1000);
	
setInterval( function() {
	var hours = new Date().getHours();
	$(".hours, .hour").html(( hours < 10 ? "0" : "" ) + hours);
    }, 1000);
	
//-----------------------------------------------------------------------------------
//	2.	Fix Classes after Validate Login
//-----------------------------------------------------------------------------------

$('.submit').click(function() {
	var ValPassword = $('#password').val() === 'admin';
    if (ValPassword === true) {
		$('input[type=password]').addClass('valid');
		$('.tooltip-pass').hide();
		$('.submit').removeClass('submit').addClass('charge');
		$('#pageLogin').addClass('initLog').delay(1900).queue(function() { $(this).removeClass('initLog').addClass('initLogExit'); $(this).dequeue(); });;
		$('#page, #head').delay(2500).queue(function() { $(this).addClass('vis'); $(this).dequeue(); });
		$('.window').delay(3000).queue(function() { $(this).addClass('windows-vis'); $(this).dequeue(); });
		event.preventDefault();
    }
    else {
		$('.tooltip-pass').hide();
		$('input[type=password]').select();
    	$('.validate').addClass('error').delay(210).queue(function() { $(this).removeClass('error'); $(this).dequeue(); $('.tooltip-pass').show(); });
			return false;
    	}
});

//-----------------------------------------------------------------------------------
//	3.	Draggable Windows
//-----------------------------------------------------------------------------------

$('.content').remove();  //>?

// var a = 3;

$('.content,.specific,.project,.share,.peruser').draggable({ handle: '.title-inside', start: function(event, ui) { $(this).css("z-index", a++); }});
$(".window").draggable({ handle: '.titleInside, .title-mac, .tab, #toolbar, #view', refreshPositions: true, start: function(event, ui) { $(this).css("z-index", a++); } });
// containment: 'window',

$('.folder').draggable({ handle: '.icon', start: function(event, ui) { $(this).css("z-index", a++); }});


// $(".finder").resizable();
$('.content,.specific,.project,.share,.peruser').resizable({
	handles: "n, e, s, w, ne, se, sw, nw"
});

// $( "#droppable" ).droppable({});


$( '.folder' ).dblclick(function() {

	console.log("HEY HEY ")
	var path = $( this ).data('path');
	console.log(path)

	add_to_page('/component?directory='+path+'&id=folder'+Math.round(Math.random()*9990) );



});

// TODO - double click text file
// TODO - double click image
// TODO - double click video file
// TODO - double click mp3 file



//-----------------------------------------------------------------------------------
//	4.	Dock
//-----------------------------------------------------------------------------------

$('.dock ul li').hover(
	function(){
		$(this).addClass('ok').prev().addClass('prev').prev().addClass('prev-ancor');
		$(this).addClass('ok').next().addClass('next').next().addClass('next-ancor');
	},
	function(){
		$('.dock ul li').removeClass('ok prev next next-ancor prev-ancor');
	}
);

//-----------------------------------------------------------------------------------
//	5.	Hide and Close
//-----------------------------------------------------------------------------------
var left = 50 + '%';
var top = 15 + '%';
var item = $('<div class="fresh"></div>').hide();
var itemR = $('<div class="fresh"></div>').hide();


$("a[data-rel=close]").click(function(e) {
    e.preventDefault();
    $(this.hash).fadeOut(200, function() {
		$(this).css({ top: top, left: left });
	});
});

$("a[data-rel=show]").click(function(e) {
    e.preventDefault();
    $(this.hash).show();
});

$(".dock li a[data-rel=showOp]").click(function(e) {
    e.preventDefault();
	$(this).addClass('bounce').delay(1600).queue(function() { $(this).removeClass('bounce'); $(this).append(item); item.fadeIn(500); $(this).dequeue(); });
    $("#warning").delay(1630).queue(function() { $(this).show(); $(this).dequeue(); });
});

$("#warning a[data-rel=close]").click(function(e) {
    e.preventDefault();
	item.fadeOut(500);
    $(this.hash).hide();
});

$(".dock li a[data-rel=showOpTrash]").click(function(e) {
    e.preventDefault();
	$(this).addClass('bounce').delay(1600).queue(function() { $(this).removeClass('bounce'); $(this).append(itemR); itemR.fadeIn(500); $(this).dequeue(); });
    $("#trash").delay(1630).queue(function() { $(this).show(); $(this).dequeue(); });
});

$("#trash a[data-rel=close]").click(function(e) {
    e.preventDefault();
	itemR.fadeOut(500);
    $(this.hash).hide();
});



//-----------------------------------------------------------------------------------
//	5.	Hide and Close
//-----------------------------------------------------------------------------------


}); 


