T = int(input())
dr=[0,0,1,-1,1,1,-1,-1]
dc=[1,-1,0,0,1,-1,1,-1]
for tc in range(1, T+1):
    arr=[]
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    ans =[1,2,3,4,5,6,7,8,9]
    cnt=0
    #r check
    for row in arr:
        if sorted(row)==ans:
            cnt+=1
    #c check
    for c in range(9):
        column = []
        for n in range(9):
            column.append(arr[0+n][c])
        if sorted(column) == ans:
            cnt+=1

    # square 확인
    for r in range(1, 9, 3):
        for c in range(1, 9, 3):
            square = [arr[r][c]]
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < 9 and 0 <= nc < 9:
                    square.append(arr[nr][nc])
            if sorted(square) == ans:  
                cnt += 1

    if cnt == 27:
        result = 1
    else:
        result = 0
    print(f'#{tc} {cnt}')