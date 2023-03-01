
function acaoBotao(){
    var nome, mensagem, idade, qtd, cont

    qtd = parseInt(prompt("Quantidade de pessoas a serem cadastradas: "))

    cont = 1
    while (cont <= qtd){
        nome = prompt("Entre com o " + cont + "º nome: ")
        idade = parseInt(prompt("Entre com a idade: "))
        if (idade >= 18){
            mensagem = " maior de idade"
        }else{
            mensagem = " menor de idade"
        }
        document.getElementById('paragrafo').innerText = nome + " você é " + mensagem
        cont ++ 
    }
}