from collections import deque

def bfs(i, j, N):
    vstd = [[0] * N for _ in range(N)]
    q = deque()
    q.append([i, j])  # 시작점
    vstd[i][j] = 1
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and vstd[wi][wj] == 0:
                q.append([wi, wj])
                vstd[wi][wj] = vstd[ti][tj] + 1
    return 0

def findstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

for tc in range(1, 10 + 1):
    t=int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = findstart(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')

