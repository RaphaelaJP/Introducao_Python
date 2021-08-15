valor = float(input("Digite um valor: "))
from math import trunc
novoValor = trunc(valor)
print('O valor é {}, e a parte inteira é: {}.'.format(valor, novoValor))