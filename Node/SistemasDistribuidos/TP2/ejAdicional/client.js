const a = require('net')

const client = new net.Socket();


const connect = client.connect(8080,'localhost', () =>{
    client.write('Hola');
})

client.on('data', (data) =>{
    console.log(data)
})


client.on('close', ()=>{
    console.log("closed")

})

