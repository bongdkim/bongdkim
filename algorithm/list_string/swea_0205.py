# 5개중 두번째 값 찾아서 빼빼는 함수
def list_second(i):
    second = arr[i-2]
    # second = 0
    for x in [-2, -1, 1, 2]:
        if arr[i+x] >= second:
            second = arr[i+x]
        # elif arr[i+x] > second:
        #     second = arr[i+x]
    return second

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    jom = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            jom += (arr[i] - list_second(i))
        else:
            pass        
    print(f'#{tc} {jom}')