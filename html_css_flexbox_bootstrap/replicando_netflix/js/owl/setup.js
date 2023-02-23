$('.owl-carousel').owlCarousel({
    //quando chegar ao final dos filmes, volta para o primeiro (true) ou não (false)
    loop:false,
    //margem entre as imagens dos filmes
    margin:15,
    //coloca o botão para rodar para o lado (true) ou não (false)
    nav:true,
    //responsive é referente ao redimensionamento das imagens de acordo com o estado da janela
    // 0, 600, 1000, é o quantitativo de pixels na tela
    // intems é o quantitativo de imagens que aparecerão caso tenha um determinado quantitativo de pixels na tela
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})