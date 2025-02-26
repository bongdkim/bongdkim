N=5
arr = [[0]*N for _ in range(N)]
nums = list(range(1, N**2+1))

dr = [0,1,0,-1]
dc = [1,0,-1,0]

r = c = 0
arr[r][c]=nums[0]
dir = 0    
for n in range(1, N**2):
    if 0<=r+dr[dir%4]<N and 0<=c+dc[dir%4]<N:
        if arr[r+dr[dir%4]][c+dc[dir%4]] != 0:
            dir += 1
            arr[r+dr[dir%4]][c+dc[dir%4]] = nums[n]
            r+=dr[dir%4]
            c+=dc[dir%4]
            continue
        arr[r+dr[dir%4]][c+dc[dir%4]] = nums[n]
        r+=dr[dir%4]
        c+=dc[dir%4]
    else:
        dir += 1
        arr[r+dr[dir%4]][c+dc[dir%4]] = nums[n]
        r+=dr[dir%4]
        c+=dc[dir%4]

for line in arr:
    print(*line)

# 신재은씨 짧은 코드 좋네요요
# T = int(input())
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]
#     num = 1
#     i, j ,d= 0, 0, 0
#  
#     while num <= N * N:
#         arr[i][j] = num
#         num +=1
#  
#         ni,nj = i+di[d] , j+dj[d]
#  
#         if not (0<=ni<N and 0<=nj<N and arr[ni][nj]==0):
#             d = (d+1) % 4
#             ni,nj = i+di[d],j+dj[d]
#  
#         i,j = ni,nj
#  
#     print(f'#{tc}')
#     for row in arr:
#         print(*row)