import sys; sys.stdin=open('input.txt')
# 최원민 코드
def dfs(v):
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)
T = int(input())
for TC in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)
    print(f'#{TC + 1} {cnt}')

#이하 박수정 코드
def dfs(n):
    visited[n] = True
    for node in graph[n]:
        if not visited[node]:
            dfs(node)
    return 1


T = int(input())
for tc in range(1, T + 1):
    n, edge = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(edge):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(f'#{tc} {count}')
#이하 김봉주코드

T=int(input())
for tc in range(1,T+1):
    N,M= map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(M)] # graph라고 받기도 하는군
    # 받은 노드를 인접리스트로
    adj_list=[[] for _ in range(N+1)]
    for node in nodes:
        adj_list[node[0]].append(node[1])
        adj_list[node[1]].append(node[0])
    # print(adj_list)
    # 이제부터 dfs?
    stack=[]
    top=-1
    groupcnt=0
    group=[]
    visited=[False]*(N+1)
    for i in range(1,N+1):
        if adj_list[i]== [] and visited[i]==False:
            groupcnt+=1
        elif adj_list[i]!= []: # 빈 리스트가 아니면
            stack.append(adj_list[i].pop())
            top+=1; visited[stack[top]]=True
            while stack: # 스택 다 사라질때까지, 인접리스트를 dfs로 탐색
                if adj_list[stack[top]]: # 리스트가 있으면
                    stack.append(adj_list[stack[top]].pop())
                    top+=1; visited[stack[top]]=True
                elif adj_list[stack[top]] ==[]: #리스트가 비었으면
                    stack.pop()
                    top-=1
                    if stack==[]:
                        groupcnt+=1
                        group=[]
                    # 또 찾고 있으면 스택 반복
                    # 없으면 하나 빼서 전에거 다시 찾기
    print(f'#{tc}', groupcnt)