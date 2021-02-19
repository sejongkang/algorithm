# n : 전체 면적 크기
# x : 목표 x 좌표
# y : 목표 Y 좌표
def solve(n, x, y):
    global result
    if x == X and y == Y:
        print(int(result))
        exit(0)
    # 면적이 1 이면 == 2**0 : 한칸이면
    if n == 1:
        result += 1
        return
    # 현재 면적 안에 없으면 스킵
    if not (x <= X < x + n and y <= Y < y + n):
        result += n * n
        return
    solve(n/2, x, y)
    solve(n/2, x, y + n /2)
    solve(n/2, x + n/2, y)
    solve(n/2, x + n/2, y + n/2)

result = 0
N, X, Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)
