# 문제 푸는 날짜: 220223
# BOJ 10828번 스택
# 분류: 자료 구조
# 난이도: 실버 4
# https://www.acmicpc.net/problem/10828
# 문제 풀이 핵심: 

import sys

stack = []
for _ in range(int(input())):
    order = sys.stdin.readline().rstrip()

    if order[:4] == 'push':
        dummy, num = order.split()
        stack.append(int(num))

    if order == 'pop':
        if stack: print(stack.pop())
        else: print(-1) # empty case
            
    if order == 'size':
        print(len(stack))

    if order == 'empty':
        if stack: print(0)
        else: print(1)
 
    if order == 'top':
        if stack: print(stack[-1])
        else: print(-1) # empty case