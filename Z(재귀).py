'''

굳이 dx, dy를 통해 2차원 배열을 초기화하고 수를 할당할 필요 없음!
'''


def solve(n, x, y):
    global result
    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if r == x and c == y + 1:
            print(result)
            return
        result += 1
        if r == x + 1 and c == y:
            print(result)
            return
        result += 1
        if r == x + 1 and c == y + 1:
            print(result)
            return
        result += 1
        return
    solve(n/2, x, y)
    solve(n / 2, x, y + n/2)
    solve(n / 2, x + n/2, y)
    solve(n / 2, x + n/2, y + n/2)


result = 0


N, r, c = map(int, input().split())
print(N, r, c)
solve(2**N, 0, 0)
