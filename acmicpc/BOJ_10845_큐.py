# 문제 푸는 날짜: 220209
# BOJ 10845번 큐
# 분류: 자료 구조
# 난이도: 실버 3
# https://www.acmicpc.net/problem/10845
# 문제 풀이 핵심: ??

from collections import deque
import sys


queue = deque([])

for i in range(int(input())):
    temp_input = sys.stdin.readline().rstrip()

    if temp_input[:4] == 'push':
        inputs = [i for i in temp_input.split()]
        queue.append(int(inputs[1]))

    if temp_input == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)

    if temp_input == 'size':
        print(len(queue))

    if temp_input == 'empty':
        if queue: print(0)
        else: print(1)

    if temp_input == 'front':
        print(queue[0])

    if temp_input == 'back':
        print(queue[-1])