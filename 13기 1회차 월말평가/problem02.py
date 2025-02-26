############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):
    
    # 보물의 종류를 셋으로 바꾸어 키에 넣을 준비
    treasure_set = set(treasure_list)
    
    # 딕셔너리 생성, 최초 값 0
    dic = {}
    for t in treasure_set:
        dic[t] = 0
    
    # 보물 갯수 카운팅
    for x in treasure_list:
        if x in treasure_set:
            dic[x] += 1
    # print(dic)        

    # 임계값 넘는지. 넘으면 cnt += 1
    threshold_cnt = 0
    for n in dic:
        if dic[n] > threshold:
            threshold_cnt += 1
        else:
            pass
    return (dic, threshold_cnt)
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))
# test = ["gold", "silver", "gold", "diamond", "coin", "coin"]
# analyze_treasures(test)

#####################################################
# 아래 테스트 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_treasures(["gold", "silver", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################
