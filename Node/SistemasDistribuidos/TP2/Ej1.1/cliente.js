const net = require('net')



//Creo el socket que enviara a una direccion ip + puerto
const client = new net.Socket();

//Conecto el socket

client.connect(8080,'localhost', () => {

    console.log('CLIENTE: Socket connected')

    //Mensaje que le envio al server
    client.write("2+2") //Los mensajes sons string!

})

//Respuesta del server
client.on('data', (data) =>{

    console.log("CLIENTE: Repuesta: " + data) //Observacion: Cuando se usa la notacion console.log("..." , data) ->me imprime el objeto buffer y no el mensaje, al contrario de lo que pasa en navegadores
    client.end()                    //Lo de arriba tiene sentido si viene un buffer, ahora que cambie el encoding no habria problema
})


//Se ejecuta despues del client.end
client.on('close', () =>{

    console.log("CLIENTE: Conection closed")

})