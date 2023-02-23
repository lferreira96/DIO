# digo de onde vou pegar e qual método vou utilizar
from televisao import TV

# digo que vou pegar do arquivo calculadora e vou utilizar o método Calculadora
from calculadora import Calculadora

# digo que vou pegar do arquivo aula08_conta_letras e vou utilizar os métodos Contador_letras e teste
from aula08_conta_letras import Contador_letras, teste

tv = TV()

print(tv.ligada)
tv.power()
print(tv.ligada)
print(tv.canal)
tv.aumenta_canal()
tv.aumenta_canal()
tv.aumenta_canal()
tv.aumenta_canal()
tv.aumenta_canal()
tv.aumenta_canal()
print(tv.canal)
tv.diminui_canal()
tv.diminui_canal()
tv.diminui_canal()
tv.diminui_canal()
tv.diminui_canal()
print(tv.canal)
tv.power()

calc = Calculadora()
print(calc.soma(10,2))


lista = ['papagaio','periquito','bode']
print (Contador_letras(lista))
print (teste())