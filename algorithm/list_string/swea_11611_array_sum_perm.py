import sys; sys.stdin=open('../input.txt')

def perm(k,N,arr):
    global sumlist
    if k==N:
        sumlist.append(arr)
    else:
        for i in range(k,N):
            arr[k], arr[i] = arr[i], arr[k]
            # sumlist.append(arr)
            perm(k+1,N,arr)
            arr[k], arr[i] = arr[i], arr[k]
        # (0,3) 012 102 210
        # (1,3) 012 021 102 120 210 201
        # (2,3) 그대로 붙어서 (3,3)에 append
    
T = int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    sumlist=[]
    
    perm(0, N, [0,1,2])
    print(sumlist)
    for r in range(N):
        for c in range(N):
            pass
    result = min(sumlist)
    print(f'#{tc} {result}')