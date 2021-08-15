from random import randint
vetorV = []
vetorW = vetorV

for contador in range(0, 15):
    contador = randint(0, 15)
    vetorV.append(contador)

print(f'os valores do vetor V são: {vetorV}')
print('====== Ordenando o vetor W, de forma decrescente... ======')
vetorW.sort(reverse = True)
print(f'o vetorW é composto por: {vetorW}')