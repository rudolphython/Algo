N = int(input())

arr = [0]*(N+1)

arr[0] = 0
arr[1] = 1

for i in range(2, len(arr)):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N])