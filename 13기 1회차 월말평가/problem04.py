############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    
    # 빈 리스트 먼저 처리
    if items_list == []:
        return ([], (0, 0))
    
    # 중복 제거는 set으로
    else: 
        new_list = list(set(items_list))
        # 양수합 음수합 초기값 선정
        pros = 0
        cons = 0
        # 중복제거된 리스트가 정수가 아니면 패스, 양, 음수이면 각 합에 더해줌
        for x in new_list:
            if type(x) != int:
                pass
            elif x > 0: 
                pros += x
            elif x < 0:
                cons += x 
        return (new_list, (pros, cons))
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################
