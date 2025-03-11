import sys; sys.stdin=open('input.txt')
N=int(input())
L=[0]*(V+1)
R=[0]*(V+1)
G=[0]*(V+1)
adj=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int, input().split())
    adj[a]=b
    adj[b]=a
