const express = require('express')

const app = express();

const PORT = 3000;

const caluladoraRouter = require('./app/routes/calculadora')
 
app.use(caluladoraRouter) //Usa las rutas que se estan exportando del arch carlculadra

app.listen(PORT, () =>{
    console.log("Iniciando!")
})

