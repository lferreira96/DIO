function acaoBotao(){
    var numero, fatorial;

    numero = parseInt(prompt("Nº para calcular o fatorial: "));
    fatorial = 1;
    for (var cont=1;cont<=numero;cont++){
        fatorial = fatorial * cont;
    }
    document.getElementById('paragrafo').innerText = "O fatorial do número " + numero + " é: " + fatorial;

}