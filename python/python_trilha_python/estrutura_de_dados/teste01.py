''' 
C = int(input("Nº de testes: ")) 
for i in range (C): 
  N = int(input("Número: "))
  if (N<8000):
    print('Inseto!')
  else:
    print('Mais de 8000')
'''

a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
  if b == 'ave':
    if c == 'carnivoro':
      print('aguia')
    else:
      print('pomba')
  else:
    if c == 'onivoro':
      print('homem')
    else:
      print('vaca')
else:
  if b == 'inseto':
    if c == 'hematofogo':
      print('pulga')
    else:
      print('lagarta')
  else:
    if c == 'hematofogo':
      print('sanguessuga')
    else:
      print('minhoca')
  

