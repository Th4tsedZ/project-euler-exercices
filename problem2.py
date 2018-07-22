a = 1
b = 0
fibo = 1
sfibo = 0
while fibo <= 4000000:
    fibo = a + b
    if fibo%2==0:
        sfibo += fibo
        print(sfibo)
    a = b
    b = fibo
    fibo += 1