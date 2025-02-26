N = 5#int(input())
arr = [1,4,7,8,0] 

# 선택정렬 해보자 ㅎ 최소값 뽑아서 맨 앞으로, 그거 제외 중에 또 뽑아서 맨앞

for x in range(N-1):
    min_idx=x
    for y in range(x, N):
        # 최소값 찾기
        if arr[y] < arr[min_idx]:
            min_idx = y
    # 맨 앞이랑 자리 교체
    arr[x], arr[min_idx] = arr[min_idx], arr[x]

    print(f'#{tc} {" ".join(map(str, arr))}')