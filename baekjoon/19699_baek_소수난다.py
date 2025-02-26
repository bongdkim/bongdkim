from math import factorial as fac

M = 5
N = 3
str = '2 4 10 5 8'
Mlst = list(map(int, str))
def selectMofN(Mlst, N):
    global M
    NCMlst = [] # 리스트 담을것
    for i in range(N-M):
        lst = [] # 정수 M개 담을 것
        cnt = 0  # M번 담을 카운트
        while cnt == M:
            for j in range(N): # 이건 끝까지 담아야됨
                
# while 써서
# m개 고르면 멈추도록 돌리고
# 재귀함수 하면 어떨까

    for i in Mlst:
        lst.append(i)
    return (NCMlst)

def NCM(N, m):
    NCMlst = [] # 리스트 담을것
    lst = [] # 작은 리스트
    # cnt = 0
    # lst = [N[0], N[1], N[m-1]]
    for i in range(m):
        x = 0
        y = 0
        while y < m:

            while x < (len(N)-m): #
                lst.append(N(i+x))
                x += 1
            NCMlst.append(lst)
            # 카운트가 m이 되면 m개 추가되어 탈출
            # 큰리스트에 넣기
            lst.pop()
            y += 1
        #cnt += 1
         
    while len(lst) == (fac(len(N)) // fac(m)):


    # if cnt == m:
    #     return lst 
    # else:
    
    return NCMlst