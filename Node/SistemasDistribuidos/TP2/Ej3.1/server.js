const net = require('net');

const server = net.createServer( (socket) => { 
    console.log("SERVER: Socket conectado!");      
    
    //socket.setEncoding('utf8'); 
    
    socket.on('data',(data) =>{ 

        let rta = data.toString();
        if(rta.includes('calculadora')){ //Simulo endpoint
            cuenta = rta.substring([rta.indexOf('cuenta')+7],rta.indexOf(' HTTP'));
            rta = eval(cuenta)
            const status = '200 OK'
            const date = new Date();
            let headers = [] 
            headers.push('Content-Length: 2')
            headers.push('Content-Length: 2')
            socket.write("HTTP/1.1" + status + '\n' + date +  '\n'  + headers + '\n'  + rta)

        }

        //socket.write(String(eval(data))) Aca pondria el end u otra rta pq se me queda colfgando pero bue es un ejemplo

    })    
    
    socket.on('close', (msg) => {
        server.close()
    })
});

server.listen(8080, () =>{

    console.log("Server escuchando...")
    
})