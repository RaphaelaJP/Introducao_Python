vetorA = []
vetorB = []

for contador in range(0, 5):
    vetorA.append(int(input(f'VETOR A- Digite um valor para posição -> {contador}: ')))
    vetorB.append(int(input(f'VETOR B- Digite um valor para posição -> {contador}: ')))
    vetorC = vetorA + vetorB

print('=-' * 30)
print(f'os valores do vetor A são: {vetorA}')
print(f'os valores do vetor B são: {vetorB}')
print(f'os valores do vetor C são: {vetorC}')
print('=-' * 30, '\n')
print('Ordenando de forma decrescente o vetor C: ')
vetorC.sort(reverse = True)
print(f'os valores do vetor C são: {vetorC}')