n1 = 92
pow_n = 2
n = str(n1)
n = [i for i in n]
total = 0
for j in n:
    total += int(j)**pow_n
    pow_n += 1

print(total // n1 if total > n1  and total%n1 == 0 or total == n1 else -1)