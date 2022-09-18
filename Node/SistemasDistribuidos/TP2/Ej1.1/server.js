const net = require('net');

//El flujo de los datos es -> createServer -> server.listen() -> SERVIDOR LEVANTADO!
// Luego, llega un socket y se ejecuta el callback de createServer

const server = net.createServer( (socket) => { //Levanta el servidor. Se le pasa un callback que recibe el socket que envio una conexion a esta ip
    console.log("SERVER: Socket conectado!");           //Avisa (avisa que hay un socket conectado)
    
    socket.setEncoding('utf8'); //Para que la data venga en string
    
    socket.on('data',(data) =>{ //Evento de recepcion de data por parte del socket. 

        socket.write(String(eval(data))) //Respuesta, con el encoding en utf8. Los mensajes tienen que ser String! por eso lo casteo

    })                       
});

server.listen(8080, () =>{

    console.log("Server escuchando...")
    
})