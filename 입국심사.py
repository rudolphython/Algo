def solution(n, times):
    answer = 0
    
    # 최악의 경우의 수가 나올 것을 대비하여 right는 times에서 가장 큰 값에 n명 곱하기 
    left, right = 1, max(times) * n
    
    while left <= right:
        possible_people = 0
        mid = (left + right) // 2
        
        # mid분 안에 검사 받을 수 있는 사람을 더하기
        for time in times:
            possible_people += mid // time
            # 검사 가능한 사람이 문제에 주어진 n명 보다 많다면 break
            if possible_people >= n:
                break
        
        # 검사 가능한 사람이 더 많으니까 right를 mid보다 1 줄이고 다시 시작
        # 같다면 mid가 답
        if possible_people >= n:
            right = mid - 1
            answer = mid
        # 더 적다면 left는 mid + 1
        else :
            left = mid + 1
    
    return answer