## rcrcR (행열행열 레드)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [] #painting
    for n in range(N):
        p += [list(map(int, input().split()))]
    # print(p)    
    arr = [[0]*10 for _ in range(10)]

    for x in range(N):
        for r in range(p[x][0], p[x][2]+1):
            for c in range(p[x][1], p[x][3]+1):
                if p[x][4] == 1:
                    arr[r][c] += 1 
                else:
                    arr[r][c] += 2
    purple = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                purple += 1
    print(f'#{tc} {purple}')
