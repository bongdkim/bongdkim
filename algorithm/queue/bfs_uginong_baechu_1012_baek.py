import sys;sys.stdin=open('input.txt')
from collections import deque

dr=[0,0,1,-1]
dc=[1,-1,0,0]
def bfs(r,c):
    global visited
    q=deque()
    q.append((r,c)); visited[r][c]=1
    while q:
        tr,tc=q.popleft()
        for dir in range(4):
            nr=tr+dr[dir];nc=tc+dc[dir]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]==1 and not visited[nr][nc]:
                q.append((nr,nc)); visited[nr][nc]=1

T=int(input())
for tc in range(T):
    M,N,K=map(int, input().split())

    arr=[[0]*M for _ in range(N)]
    visited=[[0]*M for _ in range(N)]

    yxlist=[]
    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x]=1
        yxlist.append((y,x))

    # for line in arr:
    #     print(line)
    worms=0
    for r in range(N):
        for c in range(M):
            if arr[r][c]==1 and not visited[r][c]:
                bfs(r,c)
                worms+=1


    print(worms)