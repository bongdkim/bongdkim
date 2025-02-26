h, m = list(map(int, input().split()))
dm = int(input())

if (m+dm)<60:
    print(f'{h} {m+dm}')
elif (m+dm)>=60:
    while (m+dm)>=60:
        h = h+(m+dm)//60
        m = (m+dm)%60
        dm = 0
        if h >= 24:
            h=h-24
    print(f'{h} {m}')