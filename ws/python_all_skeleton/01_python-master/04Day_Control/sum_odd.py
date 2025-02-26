import sys; sys.stdin = open('input.txt')

T = int(input())  # T = 3

for tc in range(1, T + 1): # tc => 1, 2, 3 
    lst = list(map(int, input().split()))
    # 홀수만 골라내서 합을 구해야 한다.
    # lst에 저장된 개수만큼 반복해서 홀수인지 판단
    total = 0
    for val in lst:
        if val % 2 == 1:
            total += val

    print(f'#{tc} {total}')
