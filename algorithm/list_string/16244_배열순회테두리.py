T=int(input())
for tc in range(1,T+1):
    r, c, N = map(int, input().split())
    arr = [[0]*10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if (i == r and c<=j<c+(N)) or (i == r+N-1 and c<=j<c+(N)) or (j == c and r<=i<r+N) or ((j == c+N-1 and r<=i<r+N)):
                arr[i][j]+=1

    print(f'#{tc}')
    for line in arr:
        print(' '.join(map(str, line)))