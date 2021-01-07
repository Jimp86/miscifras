function desaparecelogin() {
    $("#oscurecer").fadeOut();
}

function desapareceFormulariologin () {
    $("#login").fadeOut(300, desaparecelogin);
}

function mostrarFormulariologin () {
    $("#login").fadeIn();
    $("#oscurecer").click (desapareceFormulariologin)
}

function aparecelogin (e) {
    e.preventDefault();
    $("#oscurecer").fadeIn(300, mostrarFormulariologin);
}

function desapareceRegistro () {
    $("#oscurecer").fadeOut();
}

function desapareceFormulario () {
    $("#registrar").fadeOut(300, desapareceRegistro);
}

function mostrarFormulario () {
    $("#registrar").fadeIn();
    $("#oscurecer").click (desapareceFormulario)
}

function apareceRegistro (e) {
    e.preventDefault();
    $("#oscurecer").fadeIn(300, mostrarFormulario);
}

function mostrarLoginYRegistro(){
	$("#activarLogin").click(aparecelogin);
	$("#cerrar").click(desaparecelogin);
    $("#activarRegistro").click(apareceRegistro);
}

$(document).ready (mostrarLoginYRegistro);