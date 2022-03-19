# 문제 푸는 날짜: 220318
# BOJ 1138번 한 줄로 서기
# 분류: 구현
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1138
# 문제 풀이 핵심: 

import sys

N = int(input())
memory = [int(x) for x in input().split()]
line = [sys.maxsize] * N

for i, v in enumerate(memory):
    cnt = 0
    for ind, val in enumerate(line):
        if cnt == v and val == sys.maxsize:
            line[ind] = i + 1
            break

        if val > i: cnt += 1

print(*line, sep = ' ')