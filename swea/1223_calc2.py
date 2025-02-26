import sys; sys.stdin=open('input.txt')

# 후위로 바꾸는 함수 > # 후위를 계산했던 문제
def back(mystr):
    calc=[]
    stack=[]
    top=-1
    for tok in mystr:
        if tok.isdigit(): # 숫자 넣기
            calc.append(int(tok))
        elif tok=='(':
            calc.append(tok)
        elif tok==')':
            while stack[-1] !='(':
                calc.append(stack.pop()); top -= 1
            stack.pop(); top -= 1
        elif tok=='+' or tok=='-': # 연산자 넣기
            stack.append(tok); top+=1
            while stack[-1]=='*' or stack[-1] == '/':
                calc.append(stack.pop()); top-=1
        elif tok=='*' or tok=='/':
            stack.append(tok); top+=1
    return calc



for tc in range(1, 11):
    N=int(input())
    mystr=list(input())
    print(back(mystr))