"""
출저 : 프로그래머스
문제 : 점프와 순간이동
"""


def solution(n):
    ans = 0
    

    
    while n > 1:
        if n % 2 == 1:
            n //= 2
            ans += 1
        elif n % 2 == 0:
            n //= 2
            
    if n == 1:
        ans += 1
        
    return ans