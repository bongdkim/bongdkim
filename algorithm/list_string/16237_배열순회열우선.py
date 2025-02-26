T=int(input())
for tc in range(1,T+1):
    r, c, w, h = map(int, input().split())
    numlist=[n for n in range(1,w*h+1)]
    arr = [[0]*10 for _ in range(10)]

    for i in range(h):
        for j in range(w):  
            arr[r+i][c+j] = numlist[i+j*h]
    # print(arr)
    print(f'#{tc}')
    for line in arr:
        print(' '.join(map(str, line)))