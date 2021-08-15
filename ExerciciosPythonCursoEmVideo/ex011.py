largura = float(input('Informe a Largura (Em Metros) da parede: '))
altura = float(input('Informe a Altura (Em Metros)  da parede: '))
area = largura * altura
print('A parede tem a dimenssão de {} x {} e a sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, será necessário de {}L de tinta!'.format(tinta))
