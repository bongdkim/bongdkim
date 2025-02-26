############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.

def find_sum(i, j, mat):
    try:
        C = mat[i][j] 
        E = mat[i][j+1] if 0 <= j+1 < len(mat) else 0
        W = mat[i][j-1] if 0 <= j-1 < len(mat) else 0
        S = mat[i+1][j] if 0 <= i+1 < len(mat) else 0
        N = mat[i-1][j] if 0 <= i-1 < len(mat) else 0
        return C+E+W+S+N
    except IndexError:
        pass
    # for i in range(len(mat)):
    #     for j in range(len(mat)):


def max_adjacent_sum(mat):
    M = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if M < find_sum(i, j, mat):
                M = find_sum(i, j , mat)
    return M
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
# print(find_sum(0, 0, matrix2))