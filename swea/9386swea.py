T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, list(input())))
    
    cntM = 1
    cnt = 1
    for i in range(N-1):
        if arr[i+1] == arr[i] == 1:
            cnt +=1
            cntM = cnt if (cntM<cnt) else cntM
        else:
            cntM = cnt if (cntM<cnt) else cntM
            cnt = 1        
    print(f'#{tc} {cntM}')
