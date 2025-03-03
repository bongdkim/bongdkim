import sys;sys.stdin=open('5656.txt')
from itertools import product
from copy import deepcopy

def cntblocks(arr):
    cnt=0
    for line in arr:
        cnt+=(W-line.count(0))
    return cnt

def sink(arr):
    # GPT sink
    for w in range(W):
        for h in range(H-1, -1, -1):  # 아래에서 위로 순회
            if arr[h][w] > 0:
                row = h
                while row < H-1 and arr[row + 1][w] == 0:  # 숫자가 아래로 떨어질 수 있는지 확인
                    arr[row][w], arr[row + 1][w] = arr[row + 1][w], arr[row][w]
                    row += 1
    # for w in range(W):
    #     for i in range(H-1):
    #         for h in range(i,H-1-i):
    #             if arr[i+h][w]>0 and arr[i+h+1][w]==0:
    #                 arr[i+h][w], arr[i+h + 1][w] = arr[i+h + 1][w], arr[i+h][w]

dr=[0,0,1,-1]
dc=[1,-1,0,0]
def bomb(r,c):
    n=arr[r][c]
    arr[r][c]=0
    if n==1:
        return
    elif n>1:
        for m in range(1,n):
            for dir in range(4):
                nr=r+dr[dir]*m; nc=c+dc[dir]*m
                if 0<=nr<H and 0<=nc<W:
                    bomb(nr, nc) #여기서 연쇄폭발이 일어나기 전에 sink가 돼야하는데
        # sink(arr) # 다른 위치로 이동

def top(w):
    for h in range(H):
        if arr[h][w]>=1:
            return h
    else:
        return 0

T=int(input())
for tc in range(1,T+1):
    N,W,H=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(H)]
    original_arr=deepcopy(arr)
    # N회 던져서 최대한 많은 벽돌 제거, 남은 벽돌 개수? 완전탐색
    # 중복조합
    subset=list(product([x for x in range(W)], repeat=N))
    # print(subset)
    cnt=cntblocks(arr)
    # print(f'original count: ', cnt)
    for sub in subset:
        for n in range(N):
            bomb(top(list(sub)[n]),list(sub)[n])
            sink(arr)
        # for line in arr:
        #     print(line)
        cnt = min(cnt, cntblocks(arr))
        if cnt==0:
            break
        arr=deepcopy(original_arr)
    print(f'#{tc}', cnt)
