T=int(input())
for tc in range(1,T+1):
    r, c, N = map(int, input().split())
    numlist=[n for n in range(1,N**2+1)]
    arr = [[0]*10 for _ in range(10)]

    for i in range(N):
        for j in range(N):
            arr[r+i][c+j] = numlist[i*N+j]
    # print(arr)
    print(f'#{tc}')
    for line in arr:
        print(' '.join(map(str, line)))