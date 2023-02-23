'''
    Fazendo um bloco de comentários no Python
    
'''

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    dados_atuais = datetime.now()
    #print(dados_atuais)
    #print(dados_atuais.strftime('%d/%m/% %H:%M:%S'))

    diaSemana = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    Dsmes = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    dia = dados_atuais.day
    mes = dados_atuais.month
    ano = dados_atuais.year
    print('Hoje é {}, {} de {} de {}'.format(diaSemana[dados_atuais.weekday()], dia,Dsmes[mes-1], ano))

    dataCriada = datetime(2023,2,6,13,5,00)
    print(dataCriada)

    dataTexto = '06/02/2018 13:1:10'
    dataConvertida = datetime.strptime(dataTexto, '%d/%m/%Y %H:%M:%S')
    print(dataConvertida)
    novaData = dataConvertida - timedelta(days=365)
    print(novaData)







def trabalhando_com_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print (data_atual.strftime('%d/%m/%Y')) # onde está a barra posso colocar qualquer caracter que desejo para formatar a data
    print (data_atual.strftime('%d-%m-%Y'))
    print (data_atual.strftime('%d.%m.%Y'))
    print (data_atual.strftime('%d %m %Y'))

def trabalhando_com_horas():
    horario = time(hour=12,minute=15,second=10)
    print(horario.strftime('%H:%M:%S'))
    print(horario.strftime('%c'))
    print(horario)

if __name__ == '__main__':
  '''# trabalhando_com_data()
  # trabalhando_com_horas()'''
  trabalhando_com_datetime()