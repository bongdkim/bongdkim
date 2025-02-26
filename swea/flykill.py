import sys; sys.stdin=open('input2.txt')
T=int(input())
for tc in range(1, T+1):
    N, H, W = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxkill=0
    for r in range(N):
        for c in range(N):
            sum=0
            if r+H<=N and c+W<=N:
                for y in range(H):
                    for x in range(W):
                        sum+=arr[r+y][c+x]
                for y in range(H-2):
                    for x in range(W-2):
                        sum-=arr[r+1+y][c+1+x]
                if sum >= maxkill:
                    maxkill=sum
    print(f'#{tc}', maxkill)