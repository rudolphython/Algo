'''
출저: 프로그래머스
유형: BFS
'''


def solution(maps):
    # 길이 설정
    row = len(maps)
    column = len(maps[0])
    
    # 방문 배열 세팅
    visited = [[0]*column for _ in range(row)]
    visited[0][0] = 1
    
    # q 생성
    q = [[0, 0]]

    while q:
        # now를 pop 하기
        now = q.pop(0)
        now_x = now[0]
        now_y = now[1]
        
        # 도착하면 break
        if now_x == row - 1 and now_y == column - 1:
            break
        
        # 방향설정
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            # 배열 범위 벗어나면
            if next_x >= row or next_y >= column or next_x < 0 or next_y < 0:
                continue
            # 장애물은 건너뛰고
            if maps[next_x][next_y] == 0:
                continue
            # 방문했으면 건너뛰고
            if visited[next_x][next_y] >= 1:
                continue
            
            # 모든 조건 충족 시 q에 append
            q.append([next_x, next_y])
            # 거리 확인을 위한 누적
            visited[next_x][ next_y] += visited[now_x][now_y] + 1
            
    answer = visited[row-1][column-1]
    
    if answer == 0:
        answer = -1
    return answer