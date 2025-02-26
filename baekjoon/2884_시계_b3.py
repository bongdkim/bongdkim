h, m = list(map(int, input().split()))
dm = 45

if (m-dm)>=0:
    print(f'{h} {m-dm}')
elif (m-dm)<0:
    h = h-1
    m = (m+60-dm)%60
    if h < 0:
        h=23
    print(f'{h} {m}')