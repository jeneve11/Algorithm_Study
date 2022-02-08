# 문제 푸는 날짜: 220205
# BOJ 1260번 집합
# 분류: 그래프
# 난이도: 실버 2 
# https://www.acmicpc.net/problem/1260
# 문제 풀이 핵심: DFS, BFS 구현

from collections import defaultdict, deque
import sys

dots, lines, start_point = [int(i) for i in input().split()]
graph_dict = defaultdict(list)

for _ in range(lines):
    i, v = map(int, sys.stdin.readline().rstrip().split())
    graph_dict[i].append(v)
    graph_dict[v].append(i)


# BFS
visited_BFS = []
queue = deque([start_point])

# 배열 올림차순 정렬
for i in graph_dict:
    graph_dict[i].sort()

while queue:
    node_now = queue.popleft()
    if node_now not in visited_BFS:
        visited_BFS.append(node_now)
        if node_now in graph_dict:
            queue += [i for i in graph_dict[node_now] if i not in visited_BFS]


# DFS
visited_DFS = []
stack = [start_point]

# 배열 내림차순 정렬
for i in graph_dict:
    graph_dict[i].sort(reverse=True)

while stack:
    node_now = stack.pop()
    if node_now not in visited_DFS:
        visited_DFS.append(node_now)
        if node_now in graph_dict:
            stack += [i for i in graph_dict[node_now] if i not in visited_DFS]


# 결괏값 출력
print(" ".join(str(i) for i in visited_DFS))
print(" ".join(str(i) for i in visited_BFS))