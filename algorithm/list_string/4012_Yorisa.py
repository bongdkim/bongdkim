import sys
sys.stdin=open('../input.txt')

def ssum(nums, table_sy):
    temp = 0
    for x in nums:
        for y in nums:
            if i != j:
                temp += table_sy[x][y]
    return temp

T = int(input())
for tc in range(1 , T +1):
    N = int(input())
    table_sy = []
    for _ in range(N):
        table_sy += [list(map(int, input().split()))]

    shop =[] # 재료 인덱스 쇼핑해서 담기 # 6C3 = 20개
    for i in range(1<<N): # 전체(N)중에 절반(N//2)짜리 부분집합 구하기
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(j)
        if len(subset) == N//2:
            shop.append(subset)
    print(shop)
    ls = len(shop)//2

    ssum_lstA = [ssum(lst, table_sy) for lst in shop[:len(shop)]]
    ssum_lstB = [ssum(lst, table_sy) for lst in shop[len(shop)-1:len(shop)//2-1:-1]]

    ssum_gap = [abs(a - b) for a, b in zip(ssum_lstA, ssum_lstB)]
    print(f'#{tc} {min(ssum_gap)}')
    # 이러면 0~N-1에 대한 부분집합 종류가 모두 생김. 대칭위치가 A,B 짝.
    ####################################################################
    # idxA =[]  # 20개중 앞 10개조합의 2개짜리 시너지인덱스를 만들자
    # for n in range(ls):
    #     subset = []
    #     for m in range(N // 2):
    #         for o in range(N // 2):
    #             subset.append([shop[n][m], shop[n][o]])
    #     idxA.append(subset)
    #
    # idxB = []  # 20개중 뒤 10개조합의 2개짜리 시너지인덱스를 만들자
    # for n in range(ls):
    #     subset = []
    #     for m in range(N // 2):
    #         for o in range(N // 2):
    #             subset.append([shop[-1 - n][m], shop[-1 - n][o]])
    #     idxB.append(subset)
    # print(idxB)



    # ssum_lstA = [ssum(lst) for lst in idxA]
    # ssum_lstB = [ssum(lst) for lst in idxB]
    #
    # ssum_gap = [abs(a - b) for a, b in zip(ssum_lstA, ssum_lstB)]
    # print(f'#{tc} {min(ssum_gap)}')
