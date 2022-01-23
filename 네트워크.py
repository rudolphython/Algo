def solution(n, computers):
    answer = 0 
    parent = [x for x in range(n)] # 자기 자신도 부모가 되니 초기 부모는 모두 자기 자신으로

    # find 함수
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
            
        return parent[x]
    
    # union 함수
    def union(x, y):
        root1 = find(x)
        root2 = find(y)
        parent[root2] = root1
        
    # 순회하면서 연결되어 있으면 자식으로 흡수
    for i in range(n):
        for j in range(n):
            # 연결되어 있으면
            if computers[i][j] == 1:
                # 연결되어 있는데 부모가 다르면
                if find(i) != find(j):
                    # 합침
                    union(i, j)
    
    # 예외 처리
    for k in range(n):
        parent[k] = find(k)
        
    print(parent)
    
    # 중복된 부모 제거하면 연결되어 있는 집합의 개수 계산 가능
    return len(set(parent))