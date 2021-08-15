valorInicio = int(input("informe um valor inicial: "))
valorFinal  = int(input("informe um valor final: "))

print("==========================//========================")

print("Valor Inicio:",valorInicio)
print("Valor Final:",valorFinal)
print('Resultado: '.format(valorInicio, valorFinal), end = ' ')

soma = 0
for contador in range(valorInicio, valorFinal + 1):
	print(contador, end =' ')
	soma = soma + contador
print('\nA soma de todos os valores foi: ',soma)

