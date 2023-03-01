function acionarBotao(){

    var vlr01, vlr02, result;
    var oper;

    vlr01 = parseFloat(prompt("Entre com um número qualquer: "));
    vlr02 = parseFloat(prompt("Entre com um outro número qualquer: "));
    oper = prompt("Qual operação você deseja fazer (+, -, *, /: ");

    switch (oper) {
        case '+':
            result = vlr01 + vlr02;
            break;
        case '-':
            result = vlr01 - vlr02;
            break;
        case '*':
            result = vlr01 * vlr02;
            break;
        case '/':
            result = vlr01 / vlr02;
            break;                
        default:
            alert ('Operação Inválida');
            break;
    }
    document.getElementById("paragrafo").innerText = vlr01 + " " + oper + " " + vlr02 + " = " + result
}
