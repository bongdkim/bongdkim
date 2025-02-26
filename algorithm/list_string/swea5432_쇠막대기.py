import sys
sys.stdin=open('../input.txt')

# 유경민
T = int(input())
for tc in range(1, T + 1):
    lst = input()
    iron = []
    count = 0

    for i in range(len(lst)):
        if lst[i] == '(':  # '('인 경우 append
            iron.append('(')
        elif lst[i] == ')':  # ')'인 경우
            if lst[i - 1] == '(':  # 경우1. 레이저
                iron.pop()
                count += len(iron)
            else:  # 경우2. 쇠막대
                iron.pop()
                count += 1

    print(f'#{tc} {count}')

# 김봉주 시간초과
def stickcounting(abc, i):
    if abc[i] =='*' or abc[i]==')':
        return 0
    elif abc[i]=='(':
        cntopen = 0
        cntstar = 0
        for j in range(i+1, len(abc)):
            if abc[j] == '(':
                cntopen +=1
            elif abc[j] == '*':
                cntstar += 1
            elif abc[j] == ')':
                cntopen -= 1
                if cntopen == -1:
                    # pass
                    return cntstar+1


T = int(input())
for tc in range(1,T+1):
    str = input().replace('()', '*')     # ()를 일단 찾는다. (인덱스도?)
    # print(str)
    result = 0
    for n in range(len(str)-1):
        result += stickcounting(str, n) if type(stickcounting(str, n))==int else 0

    print(f'#{tc} {result}')