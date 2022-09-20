

const sendData = () => {

    user = document.getElementById('user').value;
    msg = document.getElementById('message').value;

    document.getElementById('messageArea').append(msg);
    
    fetch('http://localhost:8080/').then( (rta) => {console.log(rta)})

}

//BIEN. Ahora entiendo lo siguiente: El javascript vanila es totalmente distinto de node. Yo aca tengo modulos para el client side.
//Yo no puedo hacer un require (PARA LIBRERIAS DE NODE). Eso es propio de node (si se puede pero hay que hacer bardo)
//Si puedo agarrar y exportar de otro .js (como por ejemplo client) e importarlo aca. Peeeero, client tampoco puede tener un require.
//Puedo usar import cambiando el type a module. (commonJs default)
//Si me quiero traer un paquete que no este en el core de JS, SI O SI TENGO QUE HACER UN SCRIPT EN HTML, DISTINTO QUE EN NODE QUE SOLO CON INSTALARLO Y EL REQUIRE ESTA.
//Para hacer una peticion desde el cliente, puedo usar fetch, y el servidor web lo armo como se me antoje. (por ejemplo con net)
