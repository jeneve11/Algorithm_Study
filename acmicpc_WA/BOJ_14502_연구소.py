# 문제 푸는 날짜: 220221
# BOJ 14502번 연구소
# 분류: 그래프
# 난이도: 골드 5
# https://www.acmicpc.net/problem/14502
# 문제 풀이 핵심: 

from collections import deque
import copy, sys

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

# 입력
N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [0, 0, 1, -1]; dy = [1, -1, 0, 0]
zero = []; one = []; two = []
mini = sys.maxsize

# 0, 1, 2 갯수 파악
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0: zero.append([i, j])
        if arr[i][j] == 1: one.append([i, j])
        if arr[i][j] == 2: two.append([i, j])


# 브루트 포스 + BFS
for k in combination(zero, 3):
    visited = []
    queue = deque(two)
    temp_arr = copy.deepcopy(arr)
    for j in range(3): temp_arr[k[j][0]][k[j][1]] = 1

    while queue:
        node = queue.popleft()
        if node not in visited:
            
            visited.append(node)    
            for i in range(4):
                try:
                    nx = node[0] + dx[i]
                    ny = node[1] + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue

                    if [nx, ny] not in visited and temp_arr[nx][ny] == 0:
                        temp_arr[nx][ny] == 2
                        queue.append([nx, ny])

                except: continue
        
    mini = min(mini, len(visited))

print(N*M - len(one) - 3 - mini)