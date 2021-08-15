produtoPreço = float(input('Informe o valor do produto? R$'))
novo = produtoPreço - (produtoPreço * 5 / 100)
print('O produto que custava {}, com o desconto de 5% custará {} R$.'.format(produtoPreço, novo))
