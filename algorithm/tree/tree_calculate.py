import sys; sys.stdin=open('input.txt')

def enq(x):
    global last
    last+=1
    heap[last]=x
    p=last//2
    c=last
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c],heap[p]
        c=p
        p//=2

def inorder(T):
    if T>N:
        return float(tree[T//2])
    elif T<=N:
        # if 2*T>N:
        #     return tree[T]
        # else:
        #
        a=inorder(2*T)
        b=inorder(2*T+1)
        if tree[T]=='+':
            return float(a)+float(b)
        elif tree[T]=='-':
            return float(a)-float(b)
        elif tree[T]=='*':
            return float(a)*float(b)
        elif tree[T]=='/':
            return float(a)/float(b)
        elif type(tree[T])==float:
            return tree[T]
for tc in range(1,10+1):
    N=int(input())
    tree=[0]*(N+1)
    for _ in range(N):
        data=list(input().split())
        tree[int(data[0])]=data[1] #if type(data[1])==str else int(data[1])
        # print(data)
    result=inorder(1)
    print(f'#{tc}', int(result))


