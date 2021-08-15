aluno1 = input('Informe o nome do primeiro aluno:')
aluno2 = input('O nome so segungo: ')
aluno3 = input('O nome do terceiro: ')
aluno4 = input('O nome do quarto aluno: ')

list = [aluno1, aluno2, aluno3, aluno4]

from random import choice
escolhido = choice(list)
print('O aluno escolhido foi: {}'.format(escolhido))
