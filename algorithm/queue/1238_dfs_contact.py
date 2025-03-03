import sys;sys.stdin=open('input.txt')
for tc in range(1,11):
    N,S=map(int, input().split())
    data=list(map(int, input().split()))
    nodes=[[data[i], data[i+1]] for i in range(0,N,2)]
    adj=[[] for _ in range(101)]
    for node in nodes:
        adj[node[0]].append(node[1])

    visited=[0]*(100+1)
    visited[S]=1
    q=[S]
    while q:
        current=q.pop(0)
        # if current==G:
        #     ans=distance[current];break
        for w in adj[current]:
            if not visited[w]:
                visited[w]=visited[current]+1
                q.append(w)
    M=max(visited)
    for n in range(len(visited)):
        if visited[n]>=M:
            result = n
    print(f'#{tc}', result)