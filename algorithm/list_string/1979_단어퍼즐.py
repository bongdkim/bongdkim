mat = []
N, K = 5, 3 #map(int, input().split())

inputdata = '''0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1'''
lines = inputdata.split('\n')
for n in range(N):
    mat.append(list(map(int, inputdata.split())))

cnt = 0
for r in range(N):
    for c in range(N):
        check(r, c, N, K, mat)

dr = [1,0]
dc = [0,1]
def check(r, c, N, K, mat):
    # dir 두개 만들고 # 던져서 연속된 1이 K개 # K+1은 0이거나 index 끝나야함함
    # r check
    global cnt
    if  c == 0 or mat[r][c-1] ==0:
        k = 0
        for dc in range(K+1):
            if mat[r][c+dc]==1:
                    k+=1
            else:
                break
        if k == K:
            if c+dc+1<N and mat[r][c+dc+1]==0:
            cnt+=1
    # 반복 뒤에 1이 또 나오거나 mat 끝인 경우 고려해야됨됨
    # c check
    if  r == 0 or mat[r-1][c] ==0:
        k = 0
        for dr in range(K+1):
            if mat[r+dr][c]==1:
                k+=1
            else:
                break
        if k == K:
            cnt+=1


    # c check
