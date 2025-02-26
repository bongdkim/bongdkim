import sys; sys.stdin=open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    for n in range(N // 2 + 1):
        if n == N // 2:
            result += arr[n][N // 2]
        elif n != N // 2:
            result += arr[n][N // 2]
            result += arr[N-1 - n][N // 2]

        for m in range(1,n+1): #1부터 하니까 바로되네, N//2일때 m=0이 여러번 더해졌군
            if n == N // 2:
                result += arr[n][N//2+m]
                result += arr[n][N//2-m]
            elif m > 0:
                result += arr[n][N // 2 - m]
                result += arr[n][N // 2 + m]
                result += arr[N-1 - n][N // 2 - m]
                result += arr[N-1 - n][N // 2 + m]
    print(f'#{tc}', result)
