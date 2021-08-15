# Aprendendo importar bibliotecas no python
# Importando toda a biblioteca math(Matemática)

import math
num = int(input('Digite um numero para descobrir a raiz quadrada: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {}, é: {}'.format(num, raiz))


print('=' * 50)

# Importando apenas um modulo especifico da biblioteca

from math import factorial
num1 = int(input('Digite um numero para desobrir o fatorial: '))
fatorial = factorial(num1)
print('O fatorial de {}, é: {}'.format(num1, fatorial))
