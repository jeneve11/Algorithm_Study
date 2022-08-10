# 문제 푸는 날짜: 220806
# BOJ 1260번 BFS와 DFS
# 분류: BFS/DFS
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1260
# 문제 풀이 핵심: alphabetical하게 방문하려면, sort 필요

from collections import defaultdict, deque

def dfs(con_dict, start):
    q = [start]
    visited = []

    while q:
        node = q.pop()
        if node in visited: continue
        for i in con_dict[node]:
            q.append(i)

        visited.append(node)

    return visited

def bfs(con_dict, start):
    q = deque([start])
    visited = []

    while q:
        node = q.popleft()
        if node in visited: continue
        for i in con_dict[node]:
            q.append(i)

        visited.append(node)

    return visited


con_dict = defaultdict(list)
N, M, start = map(int, input().split())

for i in range(M):
    a, b = map(int, input().split())
    con_dict[a].append(b)
    con_dict[b].append(a)

for i in con_dict.keys(): con_dict[i].sort()

bfs_result = bfs(con_dict, start)

for i in con_dict.keys(): con_dict[i].reverse()

print(*dfs(con_dict, start))
print(*bfs_result)