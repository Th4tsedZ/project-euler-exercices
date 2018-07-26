'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
num = 1
tot = 0
temp = 0
while num < 2000000:
    tot = 0
    for c in range(1, num+1):
        if num % c == 0:
            tot += 1
    if tot <= 2 and num != 1:
        temp += num
    num += 1
print('A soma dos números primos abaixo de 10 é: {}'.format(temp))
