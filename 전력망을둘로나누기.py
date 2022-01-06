'''
출저 : 프로그래머스
'''


import collections

def bfs(wires_dict, visited, init):
    q = collections.deque()
    q.append(init)
    visited[init] = 1
    cnt = 0
    
    while q:
        now = q.popleft()
        
        for i in range(len(wires_dict[now])):
            if visited[wires_dict[now][i]] == 0:
                q.append(wires_dict[now][i])
                visited[wires_dict[now][i]] = 1
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 987654321
    
    for i, wire in enumerate(wires):
        
        wires_dict = collections.defaultdict(list)
        visited = [0 for _ in range(n+1)]
        
        for j, tmp_wire in enumerate(wires):
            if i != j:
                wires_dict[tmp_wire[0]].append(tmp_wire[1])
                wires_dict[tmp_wire[1]].append(tmp_wire[0])
        
        cnt = 0
        for j in range(1, n+1):
            if visited[j] == 0:
                if cnt == 0:
                    cnt = bfs(wires_dict, visited, j)
                else:
                    cnt -= bfs(wires_dict, visited, j)
                    cnt = abs(cnt)
                    answer = min(answer, cnt)
    
    return answer