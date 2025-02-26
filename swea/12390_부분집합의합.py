A = [n for n in range(1, 13)]
# 12 C 3(N) 이네요 그중 합이 6(K)인 경우
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N, K = 3, 6 
    subsetlist = []
    # 부분집합 생성    # 12개중에 길이 N짜리 부분집합 구하기기
    for i in range(1<<12): #부분집합의 갯수: 2**3(2^N)
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset += [A[j]]
        if len(subset)==N:
            subsetlist += [subset]
    cnt = 0
    #print(subsetlist)
    for subset in subsetlist:
        if sum(subset) == K:
            cnt+=1
    print(f'#{tc} {cnt}')
