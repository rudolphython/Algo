'''
출저: 프로그래머스(섬 연결하기)
'''

# 크루스칼 알고리즘을 이용한 풀이

def solution(n, costs):
    answer = 0
    # 최소 가중치 선택을 위한 costs 비용 정렬
    costs.sort(key = lambda x:x[2]) # [[0, 1, 1], [1, 3, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]
    # 첫 연결을 위한 초기화
    connection = set([costs[0][0]]) # {0}
    
    # 연결된 노드의 갯수와 n이 같다면 반복 종료
    while len(connection) != n:
        # 낮은 가중치부터 시작
        for cost in costs:
            # 연결된 노드가 모두 connection에 있다면 continue
            if cost[0] in connection and cost[1] in connection:
                continue
            # 새로운 노드(연결 set에 없는)가 나타나면 connection에 업데이트
            if cost[0] in connection or cost[1] in connection:
                # update함수를 사용해서 중복된 노드가 포함되지 않게 추가
                connection.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer