num = 1
tot = 0
temp = 0
for c in range(1, 10):
    if num % c == 0:
        tot += 1
if tot <= 2 and tot !=1:
    print(num)



