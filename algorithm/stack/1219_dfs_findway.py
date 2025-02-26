import sys; sys.stdin=open('input.txt')

def dfs(v):
    visited[v]=True
    for next_node in adj[v]:
        if not visited[next_node]:
            dfs(next_node)

for tc in range(1,11):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))
    visited=[False]*100
    adj=[[] for _ in range(100)]
    for i in range(0,2*N,2):
        adj[arr[i]].append(arr[i+1])

    dfs(0)
    result=1 if visited[99]==True else 0
    print(f'#{t}', result)