T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노선 개수

    bus = []
    for i in range(N): # 버스 다니는 범위 생성
        bus += [list(map(int, input().split()))]
        
    P = int(input()) # 정류장 개수
    stop = []
    for i in range(P): # 정류장 생성
        stop += [int(input())]      

    cnt = [0]*P # 정류장에 도는 버스의 수 카운트
    for i in range(P): # 정류장 돌리기
        for j in range(N): # 버스 개수 돌리기
            if bus[j][0] <= stop[i] <= bus[j][1]:
                cnt[i] += 1

    print(f'#{tc} {" ".join(map(str, cnt))}')