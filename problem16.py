'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''
n = 2**1000
lista = [int(i) for i in str(n)]
soma = sum(lista)
print(soma)