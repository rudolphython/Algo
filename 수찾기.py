N = int(input())
arr = set(list(map(int, input().split())))
M = int(int(input()))
check = list(map(int, input().split()))


for ch in check:
    if ch not in arr:
        print('0')
    else:
        print('1')
