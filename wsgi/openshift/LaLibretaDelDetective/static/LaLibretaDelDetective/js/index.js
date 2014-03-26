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
var csrf_token = getCookie('csrftoken');


$(document).ready(function() {
	validate();
});

function revert(){
	$(".flipbox").flippyReverse();
}

function validate(){
	$("#form-name").validate({
		rules : {
			input_nombre : {
				maxlength : 25,
				required : true
			},
			input_apellidos : {
				maxlength : 50,
				required : true
			},
			input_name : {
				maxlength : 25,
				required : true
			},
			input_pass : {
				minlength : 5,
				maxlength : 16,
				required : true
			},
			input_pass_confirm : {
				minlength : 5,
				maxlength : 16,
				required : true,
				equalTo : "#input_pass"
			}
		},
		messages : {
			input_nombre : "Tu nombre debe ser de entre 1 y 25 caracteres.",
			input_apellidos : "Tus apellidos deben ser de entre 1 y 50 caracteres.",
			input_name : "Tu usuario debe ser de entre 5 y 16 caracteres.",
			input_pass : "Tu contraseña debe ser de entre 5 y 16 caracteres",
			input_pass_confirm : {
				minlength : "Tu contraseña debe ser de entre 5 y 16 caracteres",
				maxlength : "Tu contraseña debe ser de entre 5 y 16 caracteres",
				required : "Tu contraseña debe ser de entre 5 y 16 caracteres",
				equalTo : "Tus contraseñas debe coincidir"
			}			
		}
	});
}
var left = true;

function flip() {
	if (left){
		left = false;
		dir = "LEFT";
	}else{
		left = true;
		dir = "RIGHT";
	}
	$(".flipbox").flippy({
		color_target : "white",
		duration : "500",
		direction : dir,
		verso : "<div class='flipbox-container'><div class='flipbox'><form id='form-name' action='/libreta_create' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='"+csrf_token+"'><p>¡ Bienvenido Detective ! </p><p>Introduce tus datos aquí para crear tu propia libreta de detective:</p><table id='table-input'><tbody><tr><td class='label-container'><label for='input_nombre' >Nombre :</label></td><td class='input-container'><input type='text' id='input_nombre' name='input_nombre'/></td></tr><tr><td class='label-container'><label for='input_apellidos' >Apellidos :</label></td><td class='input-container'><input type='text' id='input_apellidos' name='input_apellidos'/></td></tr><tr><td class='label-container'><label for='input_name' >Nombre de detective :</label></td><td class='input-container'><input type='text' id='input_name' name='input_name'/></td></tr><tr><td class='label-container'><label for='input_pass' >Contraseña :</label></td><td class='input-container'><input type='password' id='input_pass' name='input_pass'/></td></tr><tr><td class='label-container'><label for='input_pass_repeat' >Repite tu contraseña :</label></td><td class='input-container'><input type='password' id='input_pass_confirm' name='input_pass_confirm'/></td></tr></tbody></table><input type='submit' id='input-button' value='Acceder'/></form><button onclick='flip();validate();'>Ya tengo libreta.</button></div></div>",
		onFinish : validate,
		});
}