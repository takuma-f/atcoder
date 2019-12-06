n, k = list(map(int,input().split()))
h = list(map(int,input().split()))
print(sum(list(map(lambda x: 1 if x - k >= 0 else 0, h))))

# リスト生成を[]とした場合は下記
# n,k = map(int,input().split())
# print(sum([1 for i in map(int,input().split()) if i >= k]))