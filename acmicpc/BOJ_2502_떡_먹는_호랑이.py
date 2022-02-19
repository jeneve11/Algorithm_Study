# 문제 푸는 날짜: 220219
# BOJ 2502번 떡 먹는 호랑이
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/2502
# 문제 풀이 핵심: 규칙 찾기

day, rice_cake = map(int, input().split())

days = [[0, 0], [1, 0], [0, 1]]
for _ in range(28):
    days.append([days[-2][0] + days[-1][0], days[-2][1] + days[-1][1]])

for x in range(100):
    if (rice_cake - (days[day][0] * x)) % days[day][1] == 0:
        print(x)
        print((rice_cake - (days[day][0] * x)) // days[day][1])
        break