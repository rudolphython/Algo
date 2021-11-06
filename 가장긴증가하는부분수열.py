N = int(input())

arr = list(map(int, input().split()))
dp = [1] * N

for j in range(1, len(arr)):
    for i in range(j):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))

