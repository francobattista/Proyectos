const http = require('http')

const server = http.createServer( (request,response) =>{

    console.log("Socket connected")
    let body = ''

    request.on('data',(chunk) =>{
        body += chunk; //La explicacion, es que va mandando el body de a pedazos. Entonces para un primer momento tengo un pedazo del body hasta completarlo, que lo tengo en req.on('end)
    })

    request.on('end', () => {
        console.log(request.statusCode)
        console.log(request.url)
        if(request.url == '/calculadora')
            response.end(String(eval(body)))
    })

    request.on('close', () => {
        server.close()
    })
})


server.listen(8080, () =>{
    console.log("Server listening...")
})