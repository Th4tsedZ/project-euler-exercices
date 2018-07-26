'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
c = d = 0
maior = 1
while c < 1000:
    while d < 1000:
        prod = c * d
        if str(prod) == str(prod)[::-1] and c > 100 and d > 100:
            if prod > maior:
                maior = prod
        d += 1
    d = 0
    c += 1
print(maior)