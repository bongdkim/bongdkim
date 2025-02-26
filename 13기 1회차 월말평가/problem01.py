############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    
    # sum 내장함수 대신 리스트를 for문으로 돌려 합을 구합니다.
    sum_like = 0
    for x in weekly_like_list:
        sum_like += x

    # 최대, 최소는 가장 앞 리스트를 기본 값으로 설정 후 하나씩 값을 돌며 업데이트합니다.
    max_like = weekly_like_list[0]
    min_like = weekly_like_list[0]
    
    for x in weekly_like_list:
        if x > max_like:
            max_like = x
        else:
            pass
    
    for x in weekly_like_list:
        if x < min_like:
            min_like = x
        else:
            pass

    # 평균과 차이를 구합니다.
    av = sum_like / 7
    gap = max_like - min_like
    return (av, gap)

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
