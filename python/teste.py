import requests

def RetornaDadosCep(cep):

    try:
        response = requests.get('https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx')

        '''
            Códigos de retorno:
                200 - existe
                400 - não existe
        '''

        print(response.status_code)
        print(response.text)
        print(response.json())
        dados_cep = response.json()
        print(dados_cep['logradouro'],",",dados_cep['bairro'],",", dados_cep['localidade'],",",dados_cep['uf'],",",dados_cep['cep'])

    except ConnectionError:
        print('ConnectionError')

    except Exception as ex:
        print(ex)

def RetornaDadosPokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def RetornaResponse(url):
    response = requests.get(url)
    return response.text

# Main
if __name__ == '__main__':
    # Dados do CEP

    #RetornaDadosCep('29101680')
    #RetornaDadosCep('29090010')

    # Dados Pokemon
    #dados_pokemon = RetornaDadosPokemon('pikachu')
    #traz todas as informações contidas na página
    #print(dados_pokemon)
    #traz informação que está dentro de uma página em uma subsequencia
    #print(dados_pokemon['sprites']['front_shiny'])

    dados_site = RetornaResponse('http://searchvital.com/')
    print(dados_site)

