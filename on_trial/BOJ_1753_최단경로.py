# 문제 푸는 날짜: 220331
# BOJ 1753번 최단경로
# 분류: 그래프
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1753
# 문제 풀이 핵심: 

from collections import defaultdict, deque
import sys

V, E = map(int, input().split())
start = int(input())
graph = defaultdict(dict)
dist = [sys.maxsize] * (V+1)

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = c

visited = set()
queue = deque()
queue.append((start, 0))

# BFS - deque 사용
while queue:
    node_now, dist_now = queue.popleft()
    
    # 이미 방문된 노드를 재탐색 하는 경우 차단
    if node_now in visited: continue
    visited.add(node_now)

    # dist list를 기존값과 새로운 값 중 작은 값으로 갱신
    dist[node_now] = min(dist[node_now], dist_now)

    # queue에 새로 방문되는 node들 추가
    for k, v in graph[node_now].items(): queue.append((k, dist_now + v))

for i in range(1, len(dist)): print(dist[i] if dist[i] != sys.maxsize else 'INF')