'''
문제출저 : 프로그래머스(정수삼각형)
문제유형 : DP
'''

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
                
            else :
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    answer = max(triangle[-1])
    return answer