# 문제 푸는 날짜: 220215
# BOJ 16928번 뱀과 사다리 게임
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/16928
# 문제 풀이 핵심: BFS

from collections import defaultdict, deque
import sys


ladder_num, snake_num = map(int, input().split())
way_dict = defaultdict(list)
dist_dict = defaultdict(int)
dist_dict[1] = 0

# 사다리와 뱀 정보 way_dict에 기록
for _ in range(ladder_num + snake_num):
    start, fin = map(int, sys.stdin.readline().rstrip().split())
    way_dict[start].append(fin)

# 주사위로 이동 거리 정보 way_dict에 기록
for i in range(1, 100):
    if not way_dict[i]:
        way_dict[i] += [j for j in range(i+1, i+7) if j <= 100]

# BFS - dist_dict에 거리를 기록하며 진행
visited = []
queue = deque([1])

while queue:
    node = queue.popleft()

    # 예외 처리: 사다리와 뱀을 만났을 때
    if len(way_dict[node]) == 1:
        dist_dict[way_dict[node][0]] = dist_dict[node]
        node = way_dict[node][0]
        
    if node not in visited:
        visited.append(node)
        temp_nodes = [i for i in way_dict[node] if not dist_dict[i]]

        for temp_node in temp_nodes:
            if not dist_dict[temp_node]: dist_dict[temp_node] = dist_dict[node] + 1
        
        queue += temp_nodes


# 최종 출력
print(dist_dict[100])

