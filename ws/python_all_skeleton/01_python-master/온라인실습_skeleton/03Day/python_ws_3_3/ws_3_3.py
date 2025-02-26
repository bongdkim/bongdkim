def rental_book(name, n):
    decrease_book(n)
    print(f'{name}님이{n}권을 대여')
    pass

number_of_book = 100

def decrease_book(n):
    global number_of_book
    number_of_book -= n
    print(f'남은 책:{number_of_book}')
    pass
rental_book('홍길동', 3)