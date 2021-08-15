salario = eval(input("informe o salario: "))

if (salario <= 1100):
    salario = salario + (salario * 20 / 100)
    print("salario atual: ", salario)

elif (salario > 1101 and salario <= 2200):
        salario = salario + (salario * 15 / 100)
        print("salario atual: ", salario)

elif(salario > 2201 and salario <= 3300):
    salario = salario + (salario * 10 / 100)
    print("salario atual: ", salario)

elif (salario > 3301):
    salario = salario + (salario * 5 / 100)
    print("salario atual: ", salario)