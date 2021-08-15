valor = eval(input("Informe um valor: "))

soma = 0
while(valor != 0):
	soma = soma + valor;
	valor = eval(input("Informe outro valor: "))
	if(valor == 0):
		print(" ====== Fim do programa ======")
print("O resultado da soma é: ",soma)