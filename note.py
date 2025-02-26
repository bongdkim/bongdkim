arr = [[1,2,3],[4,5,6],[7,8,9]]
seq_search(arr, N, key)
N =3
key = 5

def seq_search(arr, N, key):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == key:
                ans = 1
                break
    return 1