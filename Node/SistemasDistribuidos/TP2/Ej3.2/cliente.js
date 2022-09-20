const http = require('http')

const send = '5*3+2';

const request = http.request('http://localhost:8080/calculadora',{
    method: 'GET', headers: {
        'Content-Type': 'application/json',
        'Content-Length': String(send.length) //SOLO PARA PROBAR. NO ES NECESARIO POR AHORA PASAR HEADERS.
      }/*, body: '5*3+2'*/} , (response) =>{
        let body = '';
        
        response.on('data', (chunk) => {
            body += chunk;
        })

        response.on('end',() =>{
            console.log('Recived' + body)
        })
    
        
        response.on('close', () =>{ 

            console.log('Connection closed')

        })
    }
)


request.write(send) //ESTO ES EL BODY EN HTTP!!!!!! LO DICE EN LA DOC


request.end();