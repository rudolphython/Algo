def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x   # 합치고
        number[x] += number[y] # 합치면 네트워크 수 증가


T = int(input())

for test_case in range(1, T+1):
    parent = dict()
    number = dict()
    F = int(input())
    for i in range(F):
        a, b = input().split(' ')
        if a not in parent:
            parent[a] = a   # 없으면 자기 자신이 부모
            number[a] = 1   # 혼자니까 1명
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b) # 친구니까 유니온 함수 사용

        print(number[find(a)])
