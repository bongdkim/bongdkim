import sys; sys.stdin=open('input.txt')
sys.setrecursionlimit(100000)
def inorder(T):
    if L[T]==0 and R[T]==0:
        return tree[T]
    else:

        # if 2*T>N:
        #     return tree[T]
        # else:
        # a=inorder(2*T)
        # b=inorder(2*T+1)
        a=inorder(L[T]) # 원래 2T로 가야되는데 레프트 자식으로 보내겠음
        b=inorder(R[T])
        if type(tree[T])==float:
            return tree[T]
        elif tree[T]=='+':
            return float(a)+float(b)
        elif tree[T]=='-':
            return float(a)-float(b)
        elif tree[T]=='*':
            return float(a)*float(b)
        elif tree[T]=='/':
            return float(a)/float(b)
    # else:
    #     return T
    # elif T>N:
    #     return float(tree[T//2])
for tc in range(1,10+1):
    N=int(input())
    tree=[0]*(N+1)
    L=[0]*(N+1)
    R=[0]*(N+1)
    for _ in range(N):
        data=list(input().split())
        tree[int(data[0])]=data[1] #if type(data[1])==str else int(data[1])
        if len(data)>=3:
            L[int(data[0])]=int(data[2])
            R[int(data[0])]=int(data[3])
    # print(tree)
    # print(L)
    # print(R)
    result=inorder(1)
    print(f'#{tc}', int(result))