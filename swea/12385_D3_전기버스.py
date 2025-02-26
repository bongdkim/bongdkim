T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #한번에/종점/충전소
    charge = list(map(int, input().split())) #충전소
    stop = [0]*100
    loc = 0
    cnt = 0
    for j in range(N-1): # 정류장 돌림
        for i in range(K+1, 0, -1):
            if j+i in charge:
                loc = j+i
                cnt += 1
                continue
        if loc + K >= N:
            break    
    print(f'#{tc} {cnt}')