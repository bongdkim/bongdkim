############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
# cnt = 0
# def reverse_string(s):
#     global cnt
#     if cnt < 5:
#         s = s.replace(s[len(s)-1-cnt], s[0])
#         cnt += 1
#     else:
#         reverse_string(s)


    
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.

# 재귀함수로 못 풀었을 경우

def reverse_string(s):
    return s[::-1]

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"
#####################################################
