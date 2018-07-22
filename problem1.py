soma = 0
for c in range(1, 1000):
    if c%3 == 0 or c%5 == 0:
        soma += c
print('A soma dos multiplis de 3 ou 5 abaixo de 1000 é: {}'.format(soma))