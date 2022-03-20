# 문제 푸는 날짜: 220319
# BOJ 1932번 정수 삼각형
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1932
# 문제 풀이 핵심: 

import sys
sys.setrecursionlimit ( 10 * 6 )

height = int(input())
tree = []

for i in range(height):
    tree.append([int(x) for x in sys.stdin.readline().rstrip().split()])

for i in range(len(tree) - 1, -1, -1):
    for j in range(len(tree[i]) - 1):
        tree[i-1][j] += max(tree[i][j], tree[i][j+1])

print(tree[0][0])