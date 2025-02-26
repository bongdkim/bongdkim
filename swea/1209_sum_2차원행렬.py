T = 10
for t in range(1, T+1):
    tc = int(input())
    nums = []
    for n in range(100):
        nums += [list(map(int, input().split()))]
        
    sumlist = []
    # 행 / 열 / 대각선 돌리면서 합 넣기 
    for r in range(100):
        tsum = 0
        for c in range(100):
            tsum += nums[r][c]
        sumlist += [tsum]
    for c in range(100):
        tsum = 0
        for r in range(100):
            tsum += nums[r][c]
        sumlist += [tsum]
    tsum = 0
    for c in range(100):
        tsum += nums[c][c]
    sumlist += [tsum]
    tsum = 0
    for c in range(100):
        tsum += nums[99-c][c]
    sumlist += [tsum]
    # # 리스트 합치기
    # sumlist = rsum + csum + cross
    # 최대값 출력 max() ㅋㅋ
    print(f'#{t} {max(sumlist)}')