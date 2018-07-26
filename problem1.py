'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
soma = 0
for c in range(1, 1000):
    if c%3 == 0 or c%5 == 0:
        soma += c
print('A soma dos multiplis de 3 ou 5 abaixo de 1000 é: {}'.format(soma))