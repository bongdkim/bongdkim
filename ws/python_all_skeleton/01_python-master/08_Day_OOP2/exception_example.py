def f():
    print('f 시작')
    raise Exception('난 그만할래...')
    print('f 끝')

def g():
    print('g 시작')
    f()
    print('g 끝')

def h():
    print('h 시작')
    g()
    print('h 끝')

def start():
    print('start 시작')
    h()
    print('start 끝')

try:
    start()
except:
    print('잡았따...')
