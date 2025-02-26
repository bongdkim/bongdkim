T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int,input().split())
    # P, Pa, Pb = 400, 300, 350

    # # 페이지 생성
    # page=[n for n in range(P+1)]
    # 이진탐색
    # 반 자르고 비교, #middle기준 어디에 들어가니? 좌vs우
    # for while if 
    # 또 반 자르고 비교, 어디에 들어가니?
    # 를 몇번 반복하니? log2N번? or 찾을때까지. 
    mid = P//2
    l,r = 1,P
    acnt = 1
    while Pa != mid:
        if Pa < mid:
            r = mid        
            mid = (l+mid)//2
        else: # elif page[mid] < Pa:
            l = mid
            mid = (mid+r)//2
        acnt +=1

    mid = P//2
    l,r = 1,P
    bcnt = 1
    while Pb != mid:
        if Pb < mid:
            r = mid        
            mid = (l+mid)//2
        else: # elif page[mid] < Pa:
            l = mid
            mid = (mid+r)//2
        bcnt +=1
    # 반복 끝날때까지 카운트. 높은사람 출력~

    if acnt<bcnt:
        print(f'#{tc} A')
    elif acnt==bcnt:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')