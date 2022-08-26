//const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//console.log(arr.reverse());

////////////////////////////////////////////

/*var node5 = {
    data: [1,2], // acá puede ir cualquier dato o vacío
    next: null
}

var node4 = {
    data: [3,4], // acá puede ir cualquier dato o vacío
    next: node5
}

var node3 = {
    data: [5,6], // acá puede ir cualquier dato o vacío
    next: node4
}

var node2 = {
    data: [7,8], // acá puede ir cualquier dato o vacío
    next: node3
}

function printList(node) {
    while (node) {
        console.log(node.data);
        node = node.next;
    }
}

printList(node2);

////////

var readline = require('readline');
var circle = require('./circle/circle.js');
var rl = readline.createInterface({
input: process.stdin,
output: process.stdout
});
rl.question('Escriba el radio del círculo: ', function (r) {
console.log('El área es: ' + circle.area(r));
console.log('La circunferencia es: ' + circle.circumference(r));
rl.close();
});
*/

/////

/*
var circuloPropio = require('./circle_complete');


console.log("area:" + circuloPropio.circleArea(5));
paja de definar las otras funciones
*/

var personaObjeto = {
    nombre: "Pedro",
    edad: 22,
    casado: false,
    domicilio: {
    calle: "Alvarado",
    numero: 123,
    ciudad: "Mar del Plata",
    }
}

console.log(JSON.stringify(personaObjeto))
console.log(personaObjeto)


