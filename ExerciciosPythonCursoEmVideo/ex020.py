nome01 = input('Informe o nome do primeiro aluno: ')
nome02 = input('O nome do segundo: ')
nome03 = input('O nome do terceiro: ')
nome04 = input('O nome do quarto: ')
nome05 = input('O nome do quinto: ')
nome06 = input('O nome do sexto: ')
nome07 = input('O nome do setimo: ')
nome08 = input('O nome do oitavo: ')
nome09 = input('O nome do nono: ')
nome10 = input('O nome do decimo aluno: ')
lista = [nome01, nome02, nome03, nome04, nome05, nome06, nome07, nome08, nome09, nome10]

import random

random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
