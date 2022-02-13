# 문제 푸는 날짜: 220210
# BOJ 2869번 달팽이는 올라가고 싶다
# 분류: 수학
# 난이도: 브론즈 1
# https://www.acmicpc.net/problem/2869
# 문제 풀이 핵심: 식으로 표현

import math

day, night, stick_length = map(int, input().split())

print(math.ceil((stick_length - day) / (day - night)) + 1)