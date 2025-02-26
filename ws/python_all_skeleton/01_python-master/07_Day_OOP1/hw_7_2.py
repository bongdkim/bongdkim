# 주어진 문자열을 반복 출력하는 StringRepeater 클래스를 작성하시오. 
# 클래스에는 반복 횟수와 문자열을 인자로 받아 문자열을 반복 출력하는 repeat_string 메서드가 포함되어야 한다.

class StringRepeater:
    def __init__(self):
        # 인스턴스 변수를 생성        
        print('init 메소드 실행')

    def __del__(self):
        print('나 이제 돌아갈래~')
        
    def __str__(self):  # 매직메소드: 특정 조건일 때 인터프리터에 의해 호출
        return '이 클래스는 문자열 반복 출력하는 클래스에요.'

    def repeat_string(self, count, text):
        for _ in range(count):
            print(text)
        return self

repeater1 = StringRepeater()
return_val = repeater1.repeat_string(3, "Hello")
print(repeater1 is return_val)
