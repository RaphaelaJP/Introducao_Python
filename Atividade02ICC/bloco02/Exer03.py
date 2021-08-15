valorCompra = eval(input("informe o valor da compra: "))

if (valorCompra <= 100):
    valorCompra = valorCompra - (valorCompra * 5 / 100)
    print('Valor atual com desconto: ', valorCompra)

elif (valorCompra > 101 and valorCompra <= 150):
    valorCompra = valorCompra - (valorCompra * 7 / 100)
    print('Valor atual com desconto: ', valorCompra)

elif (valorCompra > 151 and valorCompra <= 200):
        valorCompra = valorCompra - (valorCompra * 9 / 100)
        print('Valor atual com desconto: ', valorCompra)

elif(valorCompra > 201):
        valorCompra = valorCompra - (valorCompra * 10 / 100)
        print('Valor atual com desconto: ', valorCompra)