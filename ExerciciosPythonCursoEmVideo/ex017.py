catetoOposto = float(input('Digite o tamanho do cateto oposto: '))
catetoAdjacente = float(input('Digite o tamanho do catero adjacente: '))

from math import hypot
hipotenuza = hypot(catetoOposto, catetoAdjacente)
print('A Hipotenusa vai medir: {:.2f}'.format(hipotenuza))

#De forma tradicional sem a biblioteca
#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) **(1/5)


