import sys; sys.stdin=open('input.txt')
T=int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mat=[list(map(int, input().split())) for _ in range(N)]
    result=0

    for r in range(N):
        for c in range(N):
            if c==0 or mat[r][c-1]==0:
                for k in range(K):
                    if c+k<N:
                        if mat[r][c+k]!=1:
                            break
                else:
                    if c+K==N or (c+K<N and mat[r][c+K]==0):
                        result+=1
    mat = list(map(list, zip(*mat)))
    for r in range(N):
        for c in range(N):
            if c==0 or mat[r][c-1]==0:
                for k in range(K):
                    if c+k<N:
                        if mat[r][c+k]!=1:
                            break
                else:
                    if c+K==N or (c+K<N and mat[r][c+K]==0):
                        result+=1


    print(f'#{tc}', result)