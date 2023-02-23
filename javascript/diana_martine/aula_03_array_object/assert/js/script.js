// o que são vetores ou arrays

// como declarar um array

 let array = ['string',1,true];
console.log(array);

// pode guardar vários tipos de dados
let array2 = ['string',1,true,['array1'],['array2'],['array3'],['array4']];
console.log(array2);
 
// foreach
array2.forEach(function(item, index){console.log(item, index)})

// push
array2.push('Novo Item');
console.log(array2);

array2.pop();
console.log(array2);

array2.shift();
console.log(array2);

array2.unshift('Leonardo');
console.log(array2);

console.log(array2.indexOf(true)); 

//array2.splice(0,2);
//console.log(array2);

let array4 = array2.slice(0,3);
console.log(array4);

let object = {string: 'string', number: 1, boolean: true, array: ["array"], objectInterno: {objectInterno:'objeto interno'}}
console.log(object.objectInterno.objectInterno);

var string = object.string;
console.log(string);

var arrayInterno = object.array;
console.log(arrayInterno);

var {string, boolean,  objectInterno} = object;

console.log(string, boolean, objectInterno);