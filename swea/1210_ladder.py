for _ in range(10):
    tc = int(input())
    arr=[]
    for _ in range(99):
        arr.append(list(map(int, input().split())))

    # 사다리타기 로직
    # r= 100까지 갔는데 arr[100][c]=2인 값을 찾는다.

    # c < 100 인 동안 실행
    # 좌우가 0인동안 - 내려간다(r+=1). 
    # 좌나 우에 1이 있으면 방향을 바꾼다.
    # 0을 만날때까지 간다.
    # 좌우가 0인동안 - 내려간다(r+=1). 
    def check(c):
        while r < 99:
            if 1<=c<=98: # c가 1~98인 경우
                while arr[r][c-1] or arr[r][c+1] == 0:
                    r+=1
                if arr[r][c-1] == 1:
                    while arr[r][c-1]!=0 or c-1>0:
                        c-=1
                elif arr[r][c+1] == 1:
                    while arr[r][c+1]!=0 or c+1!=99:
                        c+=1
            elif c==0: # c가 0인 경우
                while arr[r][c+1] == 0:
                    r+=1
                if arr[r][c+1] == 1:
                    while arr[r][c+1]!=0 or c+1<99:
                        c+=1
            elif c==99: # c가 99인 경우
                while arr[r][c-1] == 0:
                    r+=1
                if arr[r][c-1] == 1:
                    while arr[r][c-1]!=0 or c-1!=0:
                        c-=1

        if arr[99][c] == 2:
            return True
        elif arr[99][c] == 1:
            print(c)
            return False

    c=0
    answ=False
    while answ==False:
        r=0
        if check(c):
            answ==True
            print(f'#{tc} {c}')
            break
        c+=1
        
