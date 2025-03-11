import sys; sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int, input().split()))
    M=max(arr)
    cha=[M-x for x in arr]

    S=sum(cha)
    if S==0:
        cnt=0
    elif S==1:
        cnt=1
    elif S==2:
        cnt=2
    elif S%3==0:
        cnt=S//3*2
    elif S%3==1:
        cnt=S//3*2+1
    elif S%3==2:
        cnt=S//3*2+2
    print(f'#{tc}', cnt)