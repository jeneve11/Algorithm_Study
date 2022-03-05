# 문제 푸는 날짜: 220305
# BOJ 18111번 마인크래프트
# 분류: 
# 난이도: 실버 2
# https://www.acmicpc.net/problem/18111
# 문제 풀이 핵심:

import sys

field = []; heights = []

# 입력값 받기
N, M, blocks = map(int, input().split())
for _ in range(N): field += [int(x) for x in sys.stdin.readline().rstrip().split()]

# 모든 케이스 계산
for i in range(0, 257):
    block = blocks; time = 0
    for j in range(len(field)):
        if field[j] < i:
            block -= i - field[j]
            time += i - field[j]
        elif field[j] > i:
            block += field[j] - i
            time += 2 * (field[j] - i)

    if block >= 0: heights.append(time)
    else: heights.append(sys.maxsize)

min_so = sys.maxsize; index = -1

# 최솟값 계산 후 출력
for i, v in enumerate(heights):
    if v <= min_so:
        min_so = v
        index = i

print(min_so, index)