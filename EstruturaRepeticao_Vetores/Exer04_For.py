base = int(input("Digite a base do número: "))
expoente = int(input("Digite o expoente: "))

resultado = 0
if(expoente == 0):
	print('{} elevado á: {}, é igual á:'.format(base, expoente),1)
else:
	for contador in range(expoente):
		resultado = base ** expoente
	print('{} elevado á: {}, é igual á:'.format(base, expoente), resultado)