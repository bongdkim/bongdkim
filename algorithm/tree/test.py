from sys import setrecursionlimit
setrecursionlimit(200000)

N=int(input())
L=[0]*(N+1)
R=[0]*(N+1)
tree=[0]*(N**2); tree[1]=1
nodes=[]
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes.append((a,b))

while nodes: # 돌리며 반복
    for node in nodes:
        if node[0] in tree: # 노드 꺼내보는데 앞뒤 봤을때 트리에 있으면 넣고 없으면 패스
            if tree[tree.index(node[0])*2] !=0:
                tree[tree.index(node[0])*2+1] = node[1]
            else:
                tree[tree.index(node[0])*2] = node[1]
            nodes.remove(node)
        elif node[1] in tree: # 노드 꺼내보는데 앞뒤 봤을때 트리에 있으면 넣고 없으면 패스
            if tree[tree.index(node[1])*2] !=0:
                tree[tree.index(node[1])*2+1] = node[0]
            else:
                tree[tree.index(node[1])*2] = node[0]
            nodes.remove(node)
for x in range(2,N+1):
    print(tree[tree.index(x)//2])