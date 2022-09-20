const net = require('net')


const server = net.createServer((socket) => {

    console.log("Scoket connected");
    socket.setEncoding('utf8')
    socket.on('data', (data) =>{
        console.log(data)
    });

    
    socket.on('close', () =>{
        console.log("cerrado")
    });
    

});

server.listen(8080, () => {
    console.log("Server opened")
})
