def inorder(T):
    global mystr
    if T<=N:
        if 2*T>N:
            return tree[T]
        else:
            a=inorder(2*T)
            b=inorder(2*T+1) if type(tree[T])==float: return tree[T] elif tree[T]=='+': return float(a)+float(b) elif tree[T]=='-': return float(a)-float(b) elif tree[T]=='*': return float(a)*float(b) elif tree[T]=='/': return float(a)/float(b) elif T>N: return float(tree[T//2]) for tc in range(1,10+1): N=int(input()) tree=[0]*(N+1) for _ in range(N): data=list(input().split()) tree[int(data[0])]=data[1] #if type(data[1])==str else int(data[1]) # print(data) mystr='' result=inorder(1) print(f'#{tc}', int(result))