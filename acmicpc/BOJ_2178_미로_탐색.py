# 문제 푸는 날짜: 220206
# BOJ 2178번 미로 탐색
# 분류: 그래프
# 난이도: 실버 1
# https://www.acmicpc.net/problem/2178
# 문제 풀이 핵심: BFS 구현

from collections import defaultdict, deque
import sys

graph_dict = defaultdict(list)

n, m = [int(i) for i in input().split()]
input_str = []

for i in range(n):
    input_str.append(sys.stdin.readline().rstrip())

# graph_dict 채우기
for i in range(n):
    for j in range(m):

        # 값 확인, 0이면 건너뛰기
        if int(input_str[i][j]) == 0:
            continue
        
        # 왼쪽 확인
        if j != 0 and int(input_str[i][j-1]) == 1:
            temp_val = (m * i) + j - 1
            graph_dict[m*i + j].append(temp_val)

        # 오른쪽 확인
        if j != (m-1) and int(input_str[i][j+1]) == 1:
            temp_val = (m * i) + j + 1
            graph_dict[m*i + j].append(temp_val)

        # 위 확인
        if i != 0 and int(input_str[i-1][j]) == 1:
            temp_val = m * (i - 1) + j
            graph_dict[m*i + j].append(temp_val)


        # 아래 확인
        if i != (n-1) and int(input_str[i+1][j]) == 1:
            temp_val = m * (i + 1) + j
            graph_dict[m*i + j].append(temp_val)

# BFS
queue = deque([(0)])
dist_dict = defaultdict(int)
dist_dict[0] = 1
visited = []

while queue:
    node_now = queue.popleft()
    if node_now not in visited:
        visited.append(node_now)
        
        # 마지막 칸 도달 시 while loop 탈출
        if node_now == n * m - 1:
            break
        
        for j in [i for i in graph_dict[node_now] if i not in visited]:
            queue += [i for i in graph_dict[node_now] if i not in visited]
            dist_dict[j] = dist_dict[node_now] + 1


print(dist_dict[n*m-1])