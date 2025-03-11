'''
3
10
0011001110
10
0000100001
10
0111001111
'''

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(input())
    my=[int(x) for x in arr]

    cnt=1
    cur_max=0
    for x in range(N):
        if 0<x and my[x-1]==1 and my[x]==1:
            if cnt==0:
                cnt=1
            cnt+=1
            cur_max=cnt
        elif my[x]==0:
            cnt=0
        elif my[x]==1:
            cnt=1
            cur_max=cnt

    print(f'#{tc}', cur_max)
