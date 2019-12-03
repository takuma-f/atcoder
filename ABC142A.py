n = int(input())
print(0.5) if (n % 2 == 0) else print(1.0) if (n < 2) else print(0.5 - (1 / (2*n)) + (1 / n))
