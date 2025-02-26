import sys; sys.stdin=open('input.txt')

# 후위로 바꾸는 함수 > # 후위를 계산했던 문제
def back(mystr):
    stack=[]
    top=-1
    calc=[]
    for tok in mystr:
        if tok.isdigit():
            calc.append(int(tok))
        else:
            stack.append(tok); top+=1




for tc in range(1, 11):
    N=int(input())
    mystr=list(input())
