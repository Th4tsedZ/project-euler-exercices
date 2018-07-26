'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
n = int(input('Informe um número inteiro positivo: '))

i = 1
while(i <= n):
    if n % i == 0 and i != 1:
        n = n / i
        print(i)
    i += 1
