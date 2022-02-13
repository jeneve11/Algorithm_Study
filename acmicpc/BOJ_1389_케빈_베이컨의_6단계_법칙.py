# 문제 푸는 날짜: 220213
# BOJ 1389번 케빈_베이컨의_6단계_법칙
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1389
# 문제 풀이 핵심: BFS 구현

from collections import defaultdict, deque
import sys


num_of_men, num_of_friendship = map(int, input().split())
friendship_dict = defaultdict(set)

for _ in range(num_of_friendship):
    men_1, men_2 = map(int, sys.stdin.readline().rstrip().split())
    friendship_dict[men_1].add(men_2)
    friendship_dict[men_2].add(men_1)


min_dist = -1
min_man = -1

for man in range(num_of_men, 0, -1):
    dist_dict = defaultdict(lambda: -1)
    dist_dict[man] = 0
    dist = 0
    
    visited = []
    queue = deque([man])

    while queue:
        node_now = queue.popleft()
        if node_now not in visited:
            visited.append(node_now)
            node_not_visited = [i for i in friendship_dict[node_now] if i not in visited]
            for node in node_not_visited:
                if dist_dict[node] == -1:
                    dist_dict[node] = 1 + dist_dict[node_now]
            queue += node_not_visited

    for key in dist_dict:
        dist += dist_dict[key]

    if dist <= min_dist or min_dist == -1:
        min_man = man
        min_dist = dist

print(min_man)