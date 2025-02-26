myinput= '10 1 9 2 8 3 7 4 6 5'
N = 10
arr = list(map(int, myinput.split()))
# 정렬 하고 돌릴까 바로 돌릴까. 바로 돌리긴 힘들듯
# for i in range(N-1):
for j in range(N-1):
    for i in range(N-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
# 선택정렬 - 최솟값찾아서 i번째랑 바꾸기
new = []
for n in range(N):
    if n%2==0:
        new+=[arr[N-1-(n//2)]]
    if n%2==1:
        new+=[arr[n//2]]
print(new)
