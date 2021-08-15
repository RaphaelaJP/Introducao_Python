idade = int(input("Informe a idade: "))

if (idade != 0 and idade > 0):
	contador = 1
somaIdade = idade

while idade != 0 and idade > 0:
	idade = int(input("Informe a idade: "))
	somaIdade = somaIdade + idade
	if idade <= 0:
		print('====== FIM DO PROGRAMA ======')
		break;
	contador  =  contador + 1
mediaIdade = somaIdade / contador
print("A média das idades é: ", mediaIdade)