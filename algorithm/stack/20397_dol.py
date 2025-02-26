import sys; sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i,j= map(int, input().split())
        i-=1
        # j//=2
        for d in range(1, j+1):
            if 0<=i-d and i+d <N:
                if arr[i-d] == arr[i+d]:
                    arr[i-d] = 1-arr[i-d]
                    arr[i+d] = 1-arr[i+d]
    
    print(f'#{tc}', *arr)