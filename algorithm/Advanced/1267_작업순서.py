import sys;sys.stdin=open('input.txt')
# 시작점 (없는 값들) 찾아서 -
for tc in range(1,3):
    V,E=map(int, input().split())
    arr=list(map(int, input().split()))
    nodes=[[arr[2*i], arr[2*i+1]] for i in range(E)]
    req=[[] for _ in range(V+1)]
    for node in nodes:
        req[node[1]].append(node[0])
    starts = [n for n in range(1,V) if req[n]==[]]
    # ends=[node[1] for node in nodes]
    # adj=[[] for _ in range(V+1)]
        # adj[node[0]].append(node[1])
    # print(req);    #print(adj)
    # print("ends: ", ends)
    # starts = list(set([v for v in range(1,V+1)])-set(ends)) # 이거 메모리 많이들면 빈리스트 인덱스 가져와도
    # print("starts: ", starts)
    visited=[True]+[0]*V
    q=[]; q.extend(starts);
    for s in starts:
        visited[s]=True
    while sum(visited)<(V+1):
        for n in range(1,V+1):
            if visited[n]==True:
                pass
            elif visited[n]==False:
                if set(req[n])&set(q)==set(req[n]):
                    q.append(n);visited[n]=True
    print(f'#{tc}', *q)
