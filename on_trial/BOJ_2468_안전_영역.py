# 문제 푸는 날짜: 220329
# BOJ 2468번 안전 영역
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/2468
# 문제 풀이 핵심: 

import sys

def findSafeZone():
    return

N = int(input())
field = []

for _ in range(N): field.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in field: print(i)

for i in range(10): print(findSafeZone(i))