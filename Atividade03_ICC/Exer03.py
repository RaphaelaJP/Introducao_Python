import math
N1 = eval(input("informe um numero: "))
N2 = eval(input("informe um numero: "))

print("========= Os números primos desse intervalo são: =========")
for numPrimo in range(N1, N2):
    for contador in range(2, int(math.sqrt(numPrimo)) + 1):
        if numPrimo % contador == 0:
            break;
    else:
        print(numPrimo, "É um número primo!!")