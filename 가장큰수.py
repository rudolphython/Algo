'''
문제 출저: 프로그래머스
문제 유형: 배열
'''

def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True
    return str(int(''.join(num)))
