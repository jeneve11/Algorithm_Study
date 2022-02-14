# 문제 푸는 날짜: 220214
# BOJ 5988번 홀수일까 짝수일까
# 분류: 수학
# 난이도: 브론즈 2
# https://www.acmicpc.net/problem/5988
# 문제 풀이 핵심: EZ


import sys


for _ in range(int(input())):
    if int(sys.stdin.readline().rstrip()) % 2: print('odd')
    else: print('even')