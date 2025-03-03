import sys; sys.stdin=open('input.txt')
dr=[0,0,+1,-1]
dc=[+1,-1,0,0]
def find_peaks(arr, N):
    max_val = max(map(max, arr))
    peaks = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_val:
                peaks.append((r, c))
    return peaks

def bfs(r,c,d):
    q=[]
    visited=[False]*(N**2)
    q.append([r,c,d]); visited[N*r+c]=True
    length=0
    while q:
        cr, cc, d = q.pop(0)
        length=max(length, d)
        for dir in range(4):
            nr=cr+dr[dir]; nc=cc+dc[dir];
            # print((cr,cc), (nr,nc))
            if 0<=nr<N and 0<=nc<N and arr[cr][cc]>arr[nr][nc] and not visited[N*nr+nc]:
                q.append([nr,nc,d+1]);  # visited[N*nr+nc]=True 여기선 방문리스트에 추가만 한거고 다시 갈때 어차피 visit함
                # length=max(bfs(nr,nc,d+1),length) 각 v에서 bfs를 하는거지 (while문 도는거지) bfs를 재귀하는건 아님

    return length


T=int(input())
for tc in range(1,11):
    N,K=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    max_distance=0

    peaks=find_peaks(arr,N)
    for k in range(K + 1):
        for r in range(N):
            for c in range(N):


                arr[r][c] -=k
                for pr, pc in peaks:
                    cur_distance=bfs(pr,pc,1)
                    max_distance=max(max_distance, cur_distance)
                arr[r][c] +=k
    print(f'#{tc}', max_distance)




# def distance(r,c,h,d):
#     for dir in range(4):
#         nr = r + dr[dir]; nc = c + dr[dir];
#         if 0<=nr<N and 0<=nc<N and arr[r][c]<arr[nc][dc]: # 아닌거 자동 탈락+인덱스에러 방지
#             return distance(nr, nc, arr[nr][nc], d+1)
#     return d
# # 종결조건이 없음. 나갔으면 그냥 return 하는게 아니라..그 거리를 기록해야되는데. DFS보단 BFS가 맞음
# def cur_max(r,c,h,d):
#     loc=(r,c)
#     visited=[0 for _ in range(N**2)]
#     stack=[]
#     stack.append(loc); visitd[5*loc[0]+loc[1]]
#     while stack:
#         for dir in range(4):
#             pass
#     q=[]
#     q.append(arr[r][c]);visited[5*r+c]=1
#     while q:
#         for dir in range(4):
#             nr=r+dr[dir]; nc=c+dr[dir];
#             if nr<0 or nc<0:
#                 pass
#             if 0<=nr<N and 0<=nc<N and arr[r][c]<arr[nc][dc]:
#                 pass