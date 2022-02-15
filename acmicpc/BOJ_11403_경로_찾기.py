# 문제 푸는 날짜: 220215
# BOJ 11403번 경로 찾기
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/11403
# 문제 풀이 핵심: BFS

from collections import defaultdict, deque
import sys


way_dict = defaultdict(list)
nums = int(input())
output = []

# 그래프 인접 행렬 정보를 dictionary에 저장
for num in range(nums):
    way_dict[num] = [i for i, v in enumerate(sys.stdin.readline().rstrip().split()) if v == '1']

# BFS 실행 후 간선 정보를 output list에 저장
for num in range(nums):
    visited = []
    queue = deque(way_dict[num])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += [i for i in way_dict[node] if i not in queue]
    
    output.append(visited)

# 출력
for i in range(nums):
    for j in range(nums):
        if j in output[i]: print(1, end = ' ')
        else: print(0, end = ' ')
    print()