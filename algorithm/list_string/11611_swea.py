import sys; sys.stdin = open('../input.txt')

def backtrack(i, N, cur_sum):
    global ans
    if cur_sum>ans:
        return
    elif i>N:
        return
    elif i==N:
        if cur_sum<ans:
            ans=cur_sum
    for j in range(N):
        if visited[j]==False:
            visited[j]=True
            backtrack(i+1, N, cur_sum+arr[i][j])
            visited[j]=False


    # if i==N-1:
    #     return cur_sum
    # else:
    #     for k in range(i, N):
    #         arr[k], arr[i] = arr[i], arr[k]
    #         backtrack(i + 1, N, cur_sum)
    #         arr[k], arr[i] = arr[i], arr[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    visited=[False]*N
    backtrack(0,N,0)
    print(f'#{tc}', ans)








# def perm(k, N,arr):
#     global permlist
#     if k == N:
#         permlist.append(arr[:])
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k + 1, N,arr)
#             arr[k], arr[i] = arr[i], arr[k]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     permlist = []
#     perm(0, N, [i for i in range(N)])
#     # print(permlist)
#     sumlist=[]
#     for n in range(len(permlist)):
#         sum=0
#         for r in range(N):
#             sum+=arr[r][permlist[n][r]]
#         sumlist.append(sum)
#
#     result = min(sumlist)
#     print(f'#{tc} {result}')