from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_peaks(arr, N):
    max_val = max(map(max, arr))
    peaks = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_val:
                peaks.append((r, c))
    return peaks


def bfs(pr, pc, N):
    # 방문처리 배열
    visited = [[False] * N for _ in range(N)]

    q = deque()
    visited[pr][pc] = True
    q.append((pr, pc, 1))

    length = 0
    while q:
        r, c, cnt = q.popleft()
        length = max(length, cnt)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] < arr[r][c] and not visited[nr][nc]:
                    q.append((nr, nc, cnt + 1))

    return length


for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    peaks = find_peaks(arr, N)

    max_length = 0
    # 완전 탐색 (3중 for문) N * N * K
    for k in range(K + 1):
        for r in range(N):
            for c in range(N):
                # k는 1보다 작게 만들 수도 있음.
                # if arr[r][c] - k < 0:
                #     continue

                arr[r][c] -= k

                for pr, pc in peaks:
                    length = bfs(pr, pc, N)
                    max_length = max(max_length, length)

                arr[r][c] += k  # 복원.

    print(f"#{tc} {max_length}")
