'''
출저: 프로그래머스
'''


def solution(operations):
    q  = []
    answer = 0
    for operation in operations:
        a, b = operation.split()
        if a == 'I':
            q.append(int(b))
        elif a == 'D' and b == '1':
            if len(q) >= 1:
                q.remove(max(q))
            else:
                continue
        elif a == 'D' and b == '-1':
            if len(q) >= 1:   
                q.remove(min(q))
            else:
                continue

    if len(q) >= 1:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
        
    return answer