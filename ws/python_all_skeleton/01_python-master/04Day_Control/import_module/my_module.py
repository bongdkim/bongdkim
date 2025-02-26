GOOGLE_URL = 'https://www.google.com'

def calc_sum(a, b):
    return a + b

# 다른 곳에서 모듈로 import 될때는 실행 안됨
if __name__ == '__main__':
    print('in my_module....')
    print(__name__)
    print(calc_sum(1, 2))