import sys; sys.stdin=open('3234.txt')
from itertools import permutations

def grams(n, p, left, right):
    global cnt, memo
    if sum(left)<sum(right):
        memo.add((n,p))
        return
    elif n==N:
        cnt+=1;        return
    else:
        grams(n+1, p+[perm[n]], left+[perm[n]], right)
        grams(n+1, p+[perm[n]], left, right+[perm[n]])

def check(n,p):
    pass
    key = (n, p)
    if key in memo:
        cnt += memo[key]
        return

T=int(input())
memo=set()
for tc in range(1,T+1):
    N=int(input())
    chu=list(map(int, input().split()))
    # perms=list(permutations(chu,N))
    # print(perms)
    cnt=0
    for perm in list(permutations(chu,N)):
        # perm의 앞부분이 memoization에 있는 리스트면 pass
        if perm:
            pass
        else:
            left,right=[],[]
            left.append(perm[0])
            grams(1,perm[0],left,right)

    print(f'#{tc}', cnt)