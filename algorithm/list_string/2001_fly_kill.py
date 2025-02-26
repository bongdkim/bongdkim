mat = []
N, M = 5, 2
inputdata = '''1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3'''
lines = inputdata.split('\n')

for n in range(N):
    mat.append(list(map(int, lines[n].split())))

kill_list = []
for r in range(N-(M-1)):
    for c in range(N-(M-1)):
        kill = 0
        for y in range(M):
            kill_r = 0
            for x in range(M):
                kill_r += mat[r+y][c+x]    
            kill += kill_r
        kill_list.append(kill)

print(f'1 {max(kill_list)}')