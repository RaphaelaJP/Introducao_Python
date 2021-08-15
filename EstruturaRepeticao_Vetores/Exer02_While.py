num = int(input('Quantos termos você quer mostrar? '))
termo1 = 1
termo2 = 1
print(' ')

print('~~~~ Série de Fibonacci ~~~~')
print('{} ➝  {}'.format(termo1, termo2), end = '')
contador = 3
while contador <= num:
	termo3 = termo1 + termo2
	print(' ➝ {}'.format(termo3), end = '')
	termo1 = termo2
	termo2 = termo3
	contador = contador + 1
print('. \n === Fim do programa ===')