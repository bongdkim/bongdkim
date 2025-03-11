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
    global cnt
    if T<=N:
        inorder(2*T)
        new[T]=cnt
        cnt+=1
        inorder(2*T+1)
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    new=[0]*(N+1)
    cnt=1
    inorder(1)
    print(f'#{tc}', new[1], new[N//2])


