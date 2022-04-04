# 문제 푸는 날짜: 220404
# BOJ 1743번 음식물 피하기
# 분류: BFS
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1743
# 문제 풀이 핵심: 

from collections import deque
import sys

# 배열 순회하며 가장 큰 뭉치의 쓰레기 갯수 리턴하는 함수
def countTrash():
    ret = 0
    visited = set()

    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                visited.add((i, j))
                continue

            if (i, j) not in visited and field[i][j] == 1:
                cnt = 1
                queue = deque()
                visited.add((i, j))
                queue.append((i, j))
                while queue:
                    x_now, y_now = queue.popleft()
                    
                    for k in range(4):
                        nx = dx[k] + x_now
                        ny = dy[k] + y_now

                        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                            visited.add((nx, ny))

                            if field[nx][ny] == 1:
                                cnt += 1
                                queue.append((nx, ny))

                ret = max(ret, cnt)

    return ret

N, M, trash = map(int, input().split())
field = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 빈 필드 list 생성
for _ in range(N): field.append([0] * M)

# 쓰레기 좌표 받아서 1로 변환
for _ in range(trash):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    field[a-1][b-1] = 1

# 출력
print(countTrash())