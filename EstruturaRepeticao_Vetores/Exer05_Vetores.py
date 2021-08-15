from random import randint
vetor = []

for contador in range(0,15):
	contador = randint(0,15)
	vetor.append(contador)
print('Vetor:',vetor)
vetor.sort(reverse = True)
print('Em ordem Decrescente:',vetor)