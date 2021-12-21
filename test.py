A = [9, 3, 9, 3, 9, 7, 9]

def solution(A):
    check = []
    for temp in A:
        if temp not in check:
            check.append(temp)
        else :
            check.remove(temp)

    print(check)
    return int(check)

solution(A)
