import sys; sys.stdin=open('3234.txt')
from itertools import permutations


def grams(n, p, left, right):
    global cnt, memo
    left_sum = sum(left)
    right_sum = sum(right)

    if right_sum > left_sum:
        return
    elif n == N:
        cnt += 1
        return

    key = (n, p)
    if key in memo:
        cnt += memo[key]
        return

    grams(n + 1, p + [perm[n]], left + [perm[n]], right)
    grams(n + 1, p + [perm[n]], left, right + [perm[n]])

    memo[key] = cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    chu = list(map(int, input().split()))
    cnt = 0
    memo = {}

    for perm in permutations(chu, N):
        grams(0, perm, [], [])

    print(f'#{tc}', cnt)
