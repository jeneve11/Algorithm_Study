# 문제 푸는 날짜: 22303
# BOJ 9019번 DSLR
# 분류: 그래프 - BFS
# 난이도: 골드 4
# https://www.acmicpc.net/problem/9019
# 문제 풀이 핵심: 

from collections import deque
import sys
sys.setrecursionlimit( 10 ** 6 )

for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    queue = deque([(num1, '')])

    while True:
        crt = queue.popleft()

        # D
        temp_num = (crt[0] * 2) % 10000
        temp_order = crt[1] + 'D'

        if temp_num == num2:
            print(temp_order)
            break

        queue.append([temp_num, temp_order])

        # S
        temp_num = crt[0] - 1
        if temp_num < 0: temp_num = 10000
        temp_order = crt[1] + 'S'

        if temp_num == num2:
            print(temp_order)
            break

        queue.append([temp_num, temp_order])

        # L
        temp_num = str(crt[0])
        if len(temp_num) < 4: temp_num += '0'
        else: temp_num = temp_num[1:] + temp_num[0]

        temp_num = int(temp_num)
        temp_order = crt[1] + 'L'

        if temp_num == num2:
            print(temp_order)
            break

        queue.append([temp_num, temp_order])

        # R
        temp_num = str(crt[0])
        while len(temp_num) < 4: temp_num = '0' + temp_num
        temp_num = temp_num[-1] + temp_num[:-1]

        temp_num = int(temp_num)
        temp_order = crt[1] + 'R'

        if temp_num == num2:
            print(temp_order)
            break

        queue.append([temp_num, temp_order])        
