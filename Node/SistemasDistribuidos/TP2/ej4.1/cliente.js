const { response } = require('express');
const http = require('http')

//La otra forma de hacer la peticion es con el navegador, yendo a la ruta de abajo. Solo copiar y pegar y uala

const req = http.request('http://localhost:3000/calculadora',{method: 'GET'}, (response) =>{
    let body = ''

    response.on('data', (chunk) => {
        body += chunk;
    })

    response.on('end',() =>{
        console.log('Recived' + body)
    })


})

req.write("Hola");

req.end();