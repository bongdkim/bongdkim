############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def count_happy(diary):
    # 최초 카운트 0으로 설정했습니다.
    cnt = 0
    # enumerate 함수 설정 후 h a p p y 가 연속으로 나오면 카운트를 추가했고 인덱스에러는 패스했습니다.
    try: 
        for i, c in enumerate(diary):
            if c == 'h':
                if diary[i+1] == 'a':
                    if diary[i+2] == 'p':
                        if diary[i+3] == 'p':
                            if diary[i+4] == 'y':
                                cnt += 1
    except IndexError:
        pass
    return cnt
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_happy("I feel happy. HAPPY! so happy!"))  # 2
print(count_happy("happyhappy"))                      # 2
print(count_happy("nothing here"))                    # 0
#####################################################

