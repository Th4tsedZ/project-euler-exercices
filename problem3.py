n = int(input('Informe um número inteiro positivo: '))

i = 1
while(i <= n):
    if n % i == 0 and i != 1:
        n = n / i
        print(i)
    i += 1
