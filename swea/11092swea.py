T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    min = max = arr[0]
    minidx = 0
    maxidx = 0
    for i in range(N):
        if arr[i] < min:
            min = arr[i]
            minidx = i
        elif arr[i] >= max:
            max = arr[i]
            maxidx = i
    print(f'#{tc} {abs(minidx-maxidx)}')
