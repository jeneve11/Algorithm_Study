# 문제 푸는 날짜: 220728
# BOJ 1654번 랜선 자르기
# 분류: 이분 탐색
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1654
# 문제 풀이 핵심: 1 ~ max(lan_lines)를 다 해봐야하나? 선형으로 하면 시간초과각인데... 여기서 이분탐색을 생각해내야 함

import sys

K, N = [int(i) for i in input().split()]
lan_lines = []

for _ in range(K): lan_lines.append(int(sys.stdin.readline()))
start = 1; end = max(lan_lines)

while start <= end:
    mid = (start + end) // 2

    lan_get = 0
    for line in lan_lines:
        lan_get += (line // mid)

    if lan_get >= N: start = mid + 1
    else: end = mid - 1

print(end)
