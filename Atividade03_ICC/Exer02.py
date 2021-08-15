valor = eval(input('Informe um valor: '))
contador = 1
fatorial = 1

while(contador <= valor):
  fatorial = fatorial * contador;
  contador = contador + 1
if(valor == 0):
  print("O fatorial de:", valor,"! => É igual a:", fatorial)
else:
  print("O fatorial de:",valor,"! => É igual a:", fatorial)
