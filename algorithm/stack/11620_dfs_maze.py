import sys; sys.stdin=open('input.txt')

def start(m):
    for r in range(N):
        for c in range(N):
            if m[r][c]==2:
                return r, c
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def go(r,c):
    global result
    for dir in range(4):
        nr=r+dr[dir]; nc=c+dc[dir]
        if 0<=nr<N and 0<=nc<N and maze[nr][nc]!=1:
            if maze[nr][nc]==3:
                result=1
            else:
                maze[nr][nc]=1
                go(nr, nc)


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    maze=[list(map(int, list(input()))) for _ in range(N)]
    result = 0
    r,c= start(maze)
    go(r,c)
    print(f'#{tc}', result)
