/* var jogador1 = 0;
var jogador2 = 2;
var placar;

jogador1 != 0 && jogador2 != 0 ? console.log('Jogo valido') : console.log('Jogo inválido');

//if (jogador1 != -1){
    if (jogador1>0 && jogador2 == 0){
        console.log('Jogador 1 marcou ponto');
        placar = jogador1 > jogador2;
    } else if (jogador2 >0 && jogador1==0){
        console.log('Jogador 2 marcou ponto');
        placar = jogador2 > jogador1;
    } else{
        console.log('Ninguém marcou ponto');
    }
    console.log(placar);
    switch (placar){
        case placar = jogador1>jogador2:
            console.log('Jogador 1 ganhou');
            break;
        case placar = jogador2>jogador1:
            console.log('Jogador 2 ganhou');
            break;
        default:
            console.log('Ninguém Ganhou');
    }
//}

let array = ['valor1','valor2','valor3','valor4','valor5'];
let object = {propriedade1: 'valor1',propriedade2: 'valor2',propriedade3: 'valor3'}

// for - executa uma instrução até que ela seja falsa
for (let indice=0;indice<array.length;indice++){
    console.log(indice);
}

// for/in executa repetição a partir de uma propriedade
// com array
for(let indice2 in array){
    console.log(indice2);
}

// com object
for (indice3 in object){
    console.log(indice3);
}

// for/of executa repetição a partir de valor
// com array
for (indice4 of array){
    console.log(indice4);
}

// com object
for (indice5 of object.propriedade1){
    console.log(indice5);
}
// vai pegar por exemplo um texto e separar por letras, por isso que não dá para usar o for/of para objetos
 */
var a = 0;
while (a<10){
    a++;
    console.log(a);
}

a=0;
do{
    a++;
    console.log(a);
}while (a <10);
 