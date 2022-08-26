
const readline = require('readline');


    var jugador1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]];
    var objetivos = 5;
    var endOfGame = false;

    var iniciaJugador1 = function () {

        const r = Math.random() * 5; //ni lo use alta paja

        for(i=0; i<5; i++)
            for(j=0; j<5; j++)   
            {
                jugador1[i][j] = 0;

            } 
        
        jugador1[1][1] = 1;
        jugador1[2][2] = 1;
        jugador1[3][3] = 1;
        jugador1[4][4] = 1;
        jugador1[0][0] = 1;
    }

    var calculateC1 = function (c) {
        switch (c) {
            case 'A': return 0;
            case 'B': return 1;
            case 'C': return 2;
            case 'D': return 3;
            case 'E': return 4;
        }
    }

    var searchPlayer1 = function(coordenada1, coordenada2) {
        let flag = false;
        let c1 = calculateC1(coordenada1);
        if(1 === jugador1[c1][coordenada2]){
            flag=true;
            objetivos--;
            jugador1[c1][coordenada2] = 0;
            console.log("Le diste wachin")
        }
        else
        {
            console.log("No le diste wachin")
        }
        return flag;
        
    }

    var condiciones = function(){

    }

    var pideDatos = function () {
        return new Promise((resolve,reject) => {

            var rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });

            rl.question('Escriba coordenadas: ', function (r) {
                searchPlayer1(r[0],r[1]);
                resolve();
                rl.close();
                }
            )
        }
        )
    }

    //Maldita asincronia de java
    var startGame = async function () {
            iniciaJugador1();
            while(!endOfGame)
            {
                await pideDatos().then( () => {             
                    if(objetivos == 0){
                        console.log("Ganaste");
                        endOfGame = true;
                    }   
                });
   
                    
            }
    
        }
        
    

    startGame();

    