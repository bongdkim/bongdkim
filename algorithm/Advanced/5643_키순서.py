import sys; sys.stdin=open('5643_키순서.txt')
from collections import defaultdict, deque
# GPT가 디폴트딕트 쓰니까 시간 확줄어들음
# def dfs(graph, start, visited):
#     stack = [start]
#     count = 0
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             count += 1
#             for neighbor in graph[node]:
#                 if not visited[neighbor]:
#                     stack.append(neighbor)
#     return count
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     M = int(input())
#
#     higher = defaultdict(list)
#     lower = defaultdict(list)
#
#     for _ in range(M):
#         a, b = map(int, input().split())
#         higher[b].append(a)
#         lower[a].append(b)
#
#     cnt = 0
#     for i in range(1, N + 1):
#         visited_higher = [False] * (N + 1)
#         visited_lower = [False] * (N + 1)
#
#         high_count = dfs(higher, i, visited_higher)
#         low_count = dfs(lower, i, visited_lower)
#
#         if high_count + low_count - 1 == N:
#             cnt += 1
#
#     print(f'#{tc}', cnt)

# 김봉주 풀이 시간초과
from copy import deepcopy
#higher쪽이랑 lower쪽 BFS or DFS 해서 visited 합치기 > 자기빼고 전부 True면 아는거.

def dfshigher(n):
    visited=[False]*(N+1)
    stack=[n];visited[n]=True
    while stack:
        if higher[stack[-1]]==[]: # 빈집이면
            stack.pop()
        elif higher[stack[-1]]: # 빈집 아니면
            stack.append(higher[stack[-1]].pop()) # higher 칸 맨뒤거 뽑아서 스택에 추가하고
            visited[stack[-1]]=True # 그거 방문처리 해라
    return sum(visited)

def dfslower(n):
    visited=[False]*(N+1)
    stack=[n];visited[n]=True
    while stack:
        if lower[stack[-1]]==[]: # 빈집이면
            stack.pop()
        elif lower[stack[-1]]: # 빈집 아니면
            stack.append(lower[stack[-1]].pop()) # higher 칸 맨뒤거 뽑아서 스택에 추가하고
            visited[stack[-1]]=True # 그거 방문처리 해라
    return sum(visited)


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    M=int(input())
    nodes=[]
    for _ in range(M):
        a,b=map(int, input().split())
        nodes.append([a,b])
    originallower =[[] for _ in range(N+1)];
    originalhigher=[[] for _ in range(N+1)];
    for node in nodes:
        originallower[node[0]].append(node[1])
        originalhigher[node[1]].append(node[0])
    # print(nodes)
    print(originallower)
    print(originalhigher)

    cnt=0
    for n in range(1,N+1):
        higher=deepcopy(originalhigher);lower=deepcopy(originallower)
        if (dfshigher(n)+dfslower(n))==(N+1):
            cnt+=1
    print(f'#{tc}', cnt)