import sys;sys.stdin=open('input.txt') # 메모리 초과
from itertools import combinations
T=int(input())
for tc in range(1,T+1):
    N,K=map(int, input().split())
    arr=list(map(int, input().split()))
    combs=[]
    for i in range(1,N):
        for comb in combinations(arr,i):
            if sum(comb)==K:
                combs.append(comb)

    print(f'#{tc}', len(combs))