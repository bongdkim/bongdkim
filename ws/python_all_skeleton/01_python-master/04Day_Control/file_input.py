# 주의> SWEA에 제출할 때는 주석처리하거나 빼고 제출
import sys
sys.stdin = open('file_input.txt')

# tc 개수가 입력
T = int(input())

# 매 tc 마다 계산작업을 수행하고 답을 출력한다.
# 하나의 tc는 공백으로 구분된 정수들
for tc in range(T): # range(0, 1, 2)
    # 입력 받고
    lst = list(map(int, input().split()))
    print('-->', lst)

    # 계산 작업을 수행

    # 정답을 출력
    # ans = 0
    # print(f'#{tc + 1} {ans}')