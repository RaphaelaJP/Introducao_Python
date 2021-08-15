num1 = eval(input("Informe um valor: "))
num2 = eval(input("Informe outro valor: "))

resultado = 0
if(num1 > num2):
  resultado = num1 - num2
  print("O resultado da diferença dos números é: ", resultado)
elif(num2 > num1):
   resultado = num2 - num1
   print("O resultado da difetença dos números é: ", resultado)