# 문제 푸는 날짜: 220320
# BOJ 18242번 네모네모 시력검사
# 분류: 그래프
# 난이도: 실버 5
# https://www.acmicpc.net/problem/18242
# 문제 풀이 핵심: 

from collections import defaultdict
import sys

N, M = map(int, input().split())
picture = []

for _ in range(N):
    picture.append(sys.stdin.readline().rstrip())

sharp_list = []
sharp_dict = defaultdict(list)

for i in range(N):
    for j in range(M):
        if picture[i][j] == '#':
            sharp_list.append([i, j])
            sharp_dict[i].append(j)

side = sharp_list[-1][0] - sharp_list[0][0] + 1

if len(sharp_dict[sharp_list[0][0]]) < side: print('UP')
elif len(sharp_dict[sharp_list[-1][0]]) < side: print('DOWN')
else:
    for i in range(sharp_list[0][0], sharp_list[-1][0] + 1):
        if sharp_dict[i] == [sharp_list[0][1]]: print('RIGHT')
        elif sharp_dict[i] == [sharp_list[-1][1]]: print('LEFT')