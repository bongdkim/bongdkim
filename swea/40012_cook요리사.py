import sys
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    table_sy = []
    for _ in range(N):
        table_sy += [list(map(int, input().split()))]

    shop=[] # 재료 인덱스 담기 # 6C3 = 20개
    for i in range(1<<N): # 전체(N)중에 절반(N//2)짜리 부분집합 구하기
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset += [j]
        if len(subset)==N//2:
            shop += [subset]
    # print(shop)이러면 0~N-1에 대한 부분집합 종류가 모두 생김. 회문으로 짝.
####################################################################
    idxA =[] # 20개중 앞 10개조합의 2개짜리 시너지인덱스를 만들자
    for n in range(len(shop)//2):   
        subset=[]
        for m in range(N//2):
            for o in range(N//2):
                lst = []
                # lst += shop[n][m], shop[n][o]
                subset += [[shop[n][m], shop[n][o]]]
                # lst += [shop[n][o], shop[n][o]]
        idxA += [subset]
    # print(idxA)
    
    idxB =[] # 20개중 앞 10개조합의 2개짜리 시너지인덱스를 만들자
    for n in range(len(shop)//2):   
        subset=[]
        for m in range(N//2):
            for o in range(N//2):
                lst = []
                # lst += shop[n][m], shop[n][o]
                subset += [[shop[-1-n][m], shop[-1-n][o]]]
                # lst += [shop[n][o], shop[n][o]]
        idxB += [subset]
    # print(idxB)
    
    # idxB =[] # 20개중 앞 10개조합의 2개짜리 시너지인덱스를 만들자
    # for n in range(len(shop)//2):   
    #     lst = []
    #     for m in range(N//2):
    #         for o in range(N//2):
    #             lst += [shop[-1-n][m], shop[-1-n][o]]
    #     idxB += [lst]
    
    # idxB =[] # 20개중 뒤뒤 10개조합의 2개짜리 시너지인덱스를 만들자
    # for y in range(len(shop)//2):
    #     lst = []
    #     for k in range(1<<N//2):
    #         subset = []
    #         for l in range(N//2):
    #             if k & (1<<l):
    #                 subset += [shop[-1-y][l]]
    #         # print(subset)
    #         if len(subset)==2:
    #             lst += [subset]
    #     idxB += [lst]

####################################################################

    def ssum(lst):
        temp = 0
        for x, y in lst:
            temp += table_sy[x][y] + table_sy[y][x]
        return temp

    ssum_lstA = [ssum(lst) for lst in idxA]
    ssum_lstB = [ssum(lst) for lst in idxB]

    ssum_gap = [abs(a - b) for a, b in zip(ssum_lstA, ssum_lstB)]
    print(f'#{tc} {min(ssum_gap)}')
        # # idxA의 조합마다다 Syn합 구하는 함수
        # def ssum(list):
        #     temp = 0
        #     for _ in range(len(list)):
        #         x = list[_][0]
        #         y = list[_][1]
        #         temp += table_sy[x][y] + table_sy[y][x]
        #     return temp

        # # 이제 시너지 합 리스트에 추가하자
        # ssum_lstA=[]
        # for a in range(len(idxA)): # inxA의 리스트 내 두개 쌍의 총합을 구해야 하는건데
        #     ssum_lstA += [ssum(idxA[a])]
        # # print(ssum_lstA)
        
        # ssum_lstB=[]
        # for b in range(len(idxB)): # inxB의 리스트 내 두개 쌍의 총합을 구해야 하는건데
        #     ssum_lstB += [ssum(idxB[b])]
        # # print(ssum_lstB)

        # ssum_gap=[]
        # for z in range(len(ssum_lstA)):
        #     ssum_gap += [abs(ssum_lstA[z]-ssum_lstB[z])]
