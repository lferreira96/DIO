function calculadora(){
    // abre uma janela de pergunta
    const operacao = prompt('Escolha uma operação:\n 1 - Soma (+)\n 2 - Subtração (-)\n 3 - Multiplicação (*)\n 4 - Divisão Real\n 5 - Resto da Divisão (%)\n 6 - Potenciação (**)\n 7 - Sair'); 

    if (operacao != 1 && operacao != 2 && operacao != 3 && operacao != 4 && operacao != 5 && operacao != 6 && operacao != 7){
        alert('Opção inválida!\n Favor entrar com uma das opções válidas!');
        calculadora();
    }
alert (operacao);
if (operacao != 7){
    let numero1 = Number(prompt('Entre com o primeiro número:'));
    let numero2 = Number(prompt('Entre com o segundo número:'));
    let resultado;

    if(!numero1 || !numero2){
        alert('Favor entrar com números para fazer operações!');
        calculadora();
    }else{

    function soma(){
        resultado = numero1 + numero2;
        alert(`${numero1} + ${numero2} = ${resultado}`);
    }
    function subtracao(){
        resultado = numero1 - numero2;
        alert(`${numero1} - ${numero2} = ${resultado}`);
    }
    function multiplicacao(){
        resultado = numero1 * numero2;
        alert(`${numero1} x ${numero2} = ${resultado}`);
    }
    function divisaoReal(){
        resultado = numero1 / numero2;
        alert(`${numero1} / ${numero2} = ${resultado}`);
    }
    function restoDivisao(){
        resultado = numero1 % numero2;
        alert(`${numero1} % ${numero2} = ${resultado}`);
    }
    function potenciacao(){
        resultado = numero1 ** numero2;
        alert(`${numero1} ** ${numero2} = ${resultado}`);
    }

    function novaOperacao(){
        let opcao = prompt('Deseja fazer outra operação?\n 1 - Sim\n 2 - Não');
        if (opcao == 1){
            calculadora();
        }else if (opcao == 2){
            alert('Espero que tenha gostado.\nAté breve');
        }else{
            alert('Opção inválida!\nFavor digitar uma opção válida!');
            novaOperacao();
        }
    }

    /* if (operacao ==1){
        soma();
    }else if (operacao == 2){
        subtracao();
    }else if (operacao == 3){
        multiplicacao();
    }else if (operacao == 4){        
        divisaoReal();
    }else if (operacao == 5){        
        restoDivisao();
    }else if (operacao == 6){
        potenciacao();
    } */

    switch (operacao){
        case 1:
            soma();
            break;
        case 2:
            subtracao();
            break;
        case 3:
            multiplicacao();
            break;
        case 4:
            divisaoReal();
            break;
        case 5:
            restoDivisao();
            break;
        case 6:
            potenciacao();
            break;
        case 7:
            potenciacao();
            break;
    }
    novaOperacao();
}
}
}
calculadora();