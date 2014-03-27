// using jQuery
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	crossDomain : false, // obviates need for sameOrigin test
	beforeSend : function(xhr, settings) {
		if (!csrfSafeMethod(settings.type)) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
$(document).ready(function() {
	initializeTarea1a();

	var nombre = $('#hidden-nombre').attr('value');

	$.extend($.gritter.options, {
		position : 'middle-center', // possibilities: bottom-left, bottom-right, top-left, top-right
		fade_in_speed : 100, // how fast notifications fade in (string or int)
		fade_out_speed : 100, // how fast the notices fade out
		time : 7000 // hang on the screen for...
	});

	//single book
	var book = $('#mybook').booklet({
		closed : true,
		covers : true,
		arrows : true,
		autoCenter : true,
		hovers : false,
		manual : false,
		width : '939px',
		height : '840px',
		chapterSelector : true,
		menu : "#custom-menu",
	});

	$(".b-div-cover-back").parent().addClass('b-page-cover-back');
	$(".b-div-cover-front").parent().addClass('b-page-cover-front');

	$('input[type="submit"]').click(function(event) {
		button = $(this).attr('value');
		if (button == 'Guardar') {
			$("#form-book").submit(function(event) {
				event.preventDefault();
				$.post("/libreta_save", $(this).serialize(), function(data) {
					$.gritter.add({
						// (string | mandatory) the heading of the notification
						title : '¡ Muy bien hecho detective ' + nombre + '!',
						// (string | mandatory) the text inside the notification
						text : 'Todo tu progreso ha sido guardado en la libreta. Sigue rellenandola ahora o vuelve luego para terminarla cuando hayas conseguido más pistas ...'
					});
				});
			});
		} 
	});
	$('#button-logout').click(function() {
		if (confirm('¿Estas seguro de que quieres salir? Acuerdate que debes guardar tus respuestas antes ...')) {
			// do delete item
			$("#form-logout").submit();
		}
	});
});

