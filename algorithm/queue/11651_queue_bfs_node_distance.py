import sys; sys.stdin=open('input.txt')
from collections import deque
T=int(input())
for tc in range(1,T+1):
    V,E=map(int, input().split())
    nodes=[]
    for _ in range(E):
        a,b=map(int, input().split())
        nodes.append([a,b])
    S,G=map(int, input().split())
    adj_list=[[] for _ in range(V+1)]
    for node in nodes:
        adj_list[node[0]].append(node[1])
        adj_list[node[1]].append(node[0])
    visited=[False]*(V+1)
    visited[S]=True
    q=deque([S])
    distance=[0]*(V+1)
    ans=0
    while q:
        current=q.popleft()
        if current==G:
            ans=distance[current];break
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor]=True
                distance[neighbor]+=distance[current]+1
                q.append(neighbor)
    # else:
    #     ans=0
    print(f'#{tc}', ans)