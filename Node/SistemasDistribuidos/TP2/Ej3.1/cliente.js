const net = require('net')

const client = new net.Socket();


client.connect(8080,'localhost', () => {
    console.log('CLIENTE: Socket connected')
    cuenta = "5*3+2"
    client.write("GET /calculadora?cuenta=" + cuenta + " HTTP/1.1") 

})


client.on('data', (data) =>{
    console.log("CLIENTE: Repuesta: " + data) 

    client.end()  
})


client.on('close', () =>{
    console.log("CLIENTE: Conection closed")
})