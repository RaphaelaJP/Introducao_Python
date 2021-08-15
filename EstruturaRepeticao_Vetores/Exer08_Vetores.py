from random import randint
vetor = []

for contador in range(0,15):
	contador = randint(0,15)
	vetor.append(contador)
print('Vetor:',vetor)
print(f'O maior valor do vetor é: {max(vetor)}')
print(f'O menor valor do vetor é: {min(vetor)}')