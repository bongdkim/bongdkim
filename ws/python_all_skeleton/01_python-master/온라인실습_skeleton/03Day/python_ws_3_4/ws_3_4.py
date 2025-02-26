number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

info=[]
def create_user(name, age, address):
    increase_user()
    info.append({'name':name, 'age':age, 'address':address})
    # info.get('name', name)
    # info.get('age', age)
    # info.get('address', address)
    print(f'{name}님 환영~')
    # print(info)
    return info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# lst = list(zip(name, age, address))
list(map(create_user, name, age, address))
print(info)
# for person in lst:
#     for x in person:  

# for a, b, c in name, age, address:
#     create_user(a, b, c)