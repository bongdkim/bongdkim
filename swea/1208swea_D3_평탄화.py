def reset():
    high = arr[0]
    low = arr[0]
    ihigh = 0
    ilow = 0
    for i in range(100): #최대 최소 찾음
        if high < arr[i]:
            high = arr[i]
            ihigh = i
        elif arr[i] < low:
            low = arr[i]
            ilow = i

# Greedy
for tc in range(1,11):
    n = int(input()) # 덤프 횟수
    arr = list(map(int, input().split())) #높이
    # 가장 높은곳과 낮은곳을 찾을 때 (업데이트마다 비교해야되니까)
    # 매번 100번씩 찾을거 아니면 find나 index 함수 써야되는거 아닌가
    high = arr[0]
    low = arr[0]
    ihigh = 0
    ilow = 0
    for i in range(100): #최대 최소 찾음
        if high < arr[i]:
            high = arr[i]
            ihigh = i
        elif arr[i] < low:
            low = arr[i]
            ilow = i
    
    for i in range(n): #덤프n회 굴림
        high -= 1
        low += 1
        reset()
    





    # gap = high - low
    # dump = 0
    # sum = 0
    # for i in range(100):
    #     sum += arr[i]
    # aver = sum/100
    
    # while dump > 0:
    #     for i in range(100):
    #         if arr[i] >= aver:



    # if type(aver) == int:
    #     for i in range(100):
    #         dump += arr[i]-aver if arr[i]>=aver else 0
    # else:
    #     for i in range(100):
    #         if aver+1 < arr[i]:
    #             dump += arr[i]-int(aver+1)
    

    # for i in range(100):
    #     if type(aver) == int:
    #         dump += arr[i]-aver if arr[i]>=aver else aver-arr[i]
    #     else:
    #         dump += arr[i]-(int(aver)+1) if arr[i]>aver else int(aver)-arr[i]