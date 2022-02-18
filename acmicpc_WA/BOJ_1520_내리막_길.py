# 문제 푸는 날짜: 220218
# BOJ 1520 내리막 길
# 분류: DP? 그래프?
# 난이도: 골드 4
# https://www.acmicpc.net/problem/1520
# 문제 풀이 핵심: 



import sys

m, n = map(int, input().split())
map = []
dp = []

for _ in range(m):
    map.append([int(i) for i in sys.stdin.readline().rstrip().split()])

cnt = 0
queue = [[0, 0]]
visited = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    node = queue.pop()
    if 1:
        if node[0] == (m-1) and node[1] == (n-1):
            cnt += 1

        visited.append(node)
        for i in range(4):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if 0 > new_x or new_x >= m or 0 > new_y or new_y >= n:
                continue

            if map[new_x][new_y] < map[node[0]][node[1]]:
                queue.append([new_x, new_y])

print(cnt)