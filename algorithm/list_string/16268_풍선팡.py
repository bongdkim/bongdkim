import sys
sys.stdin=open('../input.txt')

def flower(r, c, mat):
    total = mat[r][c]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    for dir in range(4):
        for i in range(1, mat[r][c]+1):
            if 0<=r+dr[dir]*i<N and 0<=c+dc[dir]*i<M:
                total += mat[r+dr[dir]*i][c+dc[dir]*i]
    return total

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat=[(list(map(int, input().split()))) for _ in range(N)]
    # print(mat)
    sumlist = []
    for r in range(N):
        for c in range(M):
            sumlist.append(flower(r,c,mat))

    print(f'#{tc} {max(sumlist)}')