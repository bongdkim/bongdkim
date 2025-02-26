import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum=0
    already=set()
    for _ in range(M):
        i, j, d = map(int, input().split())
        for r in range(d):
            for c in range(d):
                if 0<= i+r < N and 0<= j+c < N:
                    if (i+r, j+c) not in already:
                        already.add((i+r, j+c)) # 겹치는부분 빼기 AI 도움받음
                        sum+=arr[i+r][j+c]


    result = sum
    print(f'#{tc} {result}')