function getAdmins(map){
    let admins =[];
    let user =[];
    for([key,value] of map){
        if(value === 'Admin'){
            admins.push(key);
        }else if(value === 'User'){
            user.push(key);
        }

    }
    return admins;
}


function getUsers(map){
    let user =[];
    for([key,value] of map){
        if(value === 'User'){
            user.push(key);
        }

    }
    return user;

}
const usuarios = new Map();

usuarios.set('Leonardo','Admin');
usuarios.set('Maria','Admin');
usuarios.set('Josefa','User');
usuarios.set('João','User');

console.log(getAdmins(usuarios));
console.log(getUsers(usuarios));

// Atividade 2

const meuArray = [30,30,40,5,223,2049,3034,5];

function valoresUnicos(arr){
    const mySet = new Set(arr);
    return [...mySet];
}
console.log(meuArray);
console.log(valoresUnicos(meuArray));



