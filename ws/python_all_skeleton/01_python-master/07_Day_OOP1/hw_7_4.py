# 아래 클래스를 수정하시오.

class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
        # self.number_of_people += 1 # 왜 안되지?

    def introduce(self):
        print(f'내 이름은 {self.name}이고, 나이는 {self.age}살 입니다.')



person1 = Person("Alice", 25) # <== 이름과 나이를 인자로 받는 생성자 필요
person1.introduce()           # <== 인스턴스 메소드

person2 = Person("유경민", 22) # <== 이름과 나이를 인자로 받는 생성자 필요
person2.introduce()           # <== 인스턴스 메소드
print(Person.number_of_people) # number_of_people은 클래스 변수
