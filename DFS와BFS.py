def dfs(now):
    print(now, end=" ")
    visited[now] = 1
    for next in range(1, V+1):
        if visited[next] == 1:
            continue
        dfs(next)



V, E, start = map(int, input().split())

arr = [[0]*(V+1) for _ in range(V+1)]
visited = [0]*(V+1)
for e in range(E):
    a, b = map(int, input().split())
    arr[a][b] = 1
dfs(start)


