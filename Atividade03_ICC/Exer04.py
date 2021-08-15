valorInicio = int(input("informe um valor inicial: "))
valorFinal  = int(input("informe um valor final: "))
valorIncremento = int(input("Informe o valor para ser incrementado: "))

print("==========================//========================")

resultado = valorInicio

print("Valor Inicio:",valorInicio)
print("Valor Final:",valorFinal)
print("Incremento de:", valorIncremento, "Em ",valorIncremento)
print("====== Incrementando ... ======")

for contador in range(valorInicio, valorFinal, valorIncremento):
	print(contador, end = ' ')