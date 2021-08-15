salario = eval(input("Informe o valor do salario: "))
if salario >= 2000:
    salario = salario + (salario * 10 / 100)

else:
    salario = salario + (salario * 20 / 100)
print("O salario atual: ", salario)
