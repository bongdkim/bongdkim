############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    
    # 빈 딕셔너리를 None으로 먼저 반환해줍니다.
    if animal_map == {}:
        return None
    
    # 이 외의 경우 딕셔너리를 items로 바꾸어 item의 최대값을 찾아볼까요?
    else:
        # 값의 최대값을 찾습니다.
        M = max(list(animal_map.values()))
        # 최대값의 키를 인덱싱을 통해 반환합니다. - 동일한 값이 반복될경우 테스트코드3을 참고하여 가장 앞의 값이 출력됩니다.
        M_idx = list(animal_map.values()).index(M)
        # 키값중에 최대인 인덱스를 M_animal로 정의하고 반환합니다.
        M_animal = list(animal_map.keys())[M_idx]
        return M_animal
        
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))
# dic = {"lion": 5, "tiger": 3, "elephant": 10}
# print(max(list(dic.values())))
# print(list(dic.keys()))
#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
