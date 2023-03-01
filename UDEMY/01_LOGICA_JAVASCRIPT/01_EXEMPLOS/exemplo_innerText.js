var nome, numero;

nome = prompt("Nome: ");
numero = prompt("Número: ");

//O InnerText exibirá no espaço entre a abertura e o fechamento da tag HTML
document.getElementById("paragrafo").innerText = nome + " o seu número é : " + numero;