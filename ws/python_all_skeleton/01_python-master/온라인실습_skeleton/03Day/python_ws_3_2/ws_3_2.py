number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

info={}
def create_user(name, age, address):
    increase_user()
    info.setdefault('name', name)
    info.setdefault('age', age)
    info.setdefault('address', address)
    print(f'{name}님 환영~')
    print(info)
    return info

print(f'현재 가입 된 유저 수 :{number_of_people}')
create_user('홍길동', 30, '서울')
print(f'현재 가입 된 유저 수 :{number_of_people}')