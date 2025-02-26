T = int(input())
for tc in range(1, T+1):
    N = int(input())
    so = [2,3,5,7,11]
    cnt = [0]*5
    # idx = range(N)
    for i in range(5):
        while N%(so[i]) == 0:
            N //= so[i]
            cnt[i] += 1
    print(f'#{tc} {" ".join(map(str, cnt))}')