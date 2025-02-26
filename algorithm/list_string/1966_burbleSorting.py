N = 5
str = '1 4 7 8 0'
arr = list(map(int, str.split()))

for i in range(N-1):
    for j in range(N-1-i):
        if arr[j] > arr [j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    if arr[i] > arr [i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)