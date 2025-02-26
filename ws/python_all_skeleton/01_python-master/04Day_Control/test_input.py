# input() 
# 함수가 실행되면 콘솔(터미널)에서 입력을 기다린다.
# 키보드로 입력하고 엔터키를 입력하면, 그때까지 내용을 읽는다.
# 입력한 내용은 "문자열"이다.

data = int(input())  # 정수문자열 하나를 입력
print(data)

# data = input().split()   # '10 20' 입력 => ['10', '20']
# print(data)
# 정수 2개 입력
a, b = map(int, input().split())
print(a, b)

# 정수의 개수가 많다...
lst = list(map(int, input().split()))

