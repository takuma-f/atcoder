import itertools

n = int(input())
t = list(map(int,input().split()))

print(sum(x*y for x, y in itertools.combinations(t, 2)))
