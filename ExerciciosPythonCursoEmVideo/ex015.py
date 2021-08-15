qtdKm = float(input('Informe a quantidade de Km rodados: '))
qtdDias = int(input('Informe a quantidade de dias alugados: '))
pago = (qtdDias * 60) + (qtdKm * 0.15)
print('O total a pagar é de R$ {}.'.format(pago))


