peso = eval(input("informe o peso: "))
altura = eval(input("informe altura: "))

imc = peso / (altura*altura)

if(imc <= 18.5):
    print("abaixo do peso normal: 17.5")

elif(imc > 18.5 and imc <= 25):
        print ("peso normal: 21.4")

elif(imc > 25 and imc <= 30):
        print ("acima do normal: 26.1")

elif(imc >= 30):
        print("Peso excessivo: 31.2")

print("O IMC É: ",imc)