import sys; sys.stdin=open('input.txt')
# 공통 조상 찾기 - 거꾸로 visit list (인덱스함수로 찾아보자) 교집합 중 가장 앞? - 하나
# 하위 트리갯수 구하기 - 원본에서 BFS던 DFS던 하고 visited True 갯수 구하면 됨

def parentlines(n):
    parents=[]
    def parent(n):
        for v in range(1, V+1):
            if n in adj[v]:
                parents.append(v)
                parent(v)
    parent(n)
    return parents
def bfs(n):
    q=[]
    visited=[False]*(V+1)
    q.append(n);visited[n]=True
    while q:
        t=q.pop(0)
        for w in adj[t]:
            if visited[w]==False:
                visited[w]=True
                q.append(w)
        #
        # q.append(adj[q.pop(0)]);
        # if not visited[q[-1]]:
        #     visited[q[-1]]=True
            # q.pop(0)

    return sum(visited)


T=int(input())
for tc in range(1,T+1):
    V,E,a,b=map(int, input().split())
    # print(V,E,a,b)
    adj=[[] for _ in range(V+1)]
    arr=list(map(int, input().split()))
    nodes=[[arr[2*i],arr[2*i+1]] for i in range(E)]
    for node in nodes:
        adj[node[0]].append(node[1])
    # print(adj)
    result = [x for x in parentlines(a) if x in parentlines(b)][0]
    result2= bfs(result)
    print(f'#{tc} {result} {result2}')


# 신재은 풀이
# 부모 노드 찾기
def find(node):
    for j in range(len(graph)):
        if node in graph[j]:
            parent_node.append(j)
            find(j)

    return parent_node


# 특정 노드를 루트로 하는 서브 트리 개수 구하기
def dfs(v):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

    result.append(v)
    return result


# parent_node에서 맨 처음 겹치는 값 꺼내기
def min_parent(lst):
    for i in range(len(lst) - 1):
        if lst[i] in lst[i + 1:]:
            return lst[i]


T = int(input())
for tc in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    edges = list(map(int, input().split()))
    # 그래프 생성
    graph = [[0] for _ in range(V + 1)]
    for i in range(E):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    # 방문처리 해 줄 리스트 생성
    visited = [False] * (V + 1)
    result = []
    parent_node = []

    # A,B 각각 부모 노드 찾기
    find(A)
    find(B)
    min_node = min_parent(parent_node)
    # 가장 가까운 부모 노드 dfs 개수
    cnt = dfs(min_node)

    print(f'#{tc} {min_node} {len(cnt) - 1}')