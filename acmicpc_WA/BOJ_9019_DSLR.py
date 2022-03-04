# 문제 푸는 날짜: 220303
# BOJ 9019번 DSLR
# 분류: 그래프 - BFS
# 난이도: 골드 4
# https://www.acmicpc.net/problem/9019
# 문제 풀이 핵심: 

from collections import deque
import sys
sys.setrecursionlimit( 10 ** 6 )

def findD(num):
    return (num * 2) % 10000

def findS(num):
    if num == 0: return 9999
    else: return num-1

def findL(num):
    mod_1000 = num % 1000
    ret = (num - mod_1000) // 1000
    ret = mod_1000 * 10 + ret
    return ret

def findR(num):
    mod_10 = num % 10
    ret = (num - mod_10) // 10
    ret = mod_10 * 1000 + ret
    return ret

def BFS(start, fin):
    queue = deque()
    visited = set()
    orders = ['D', 'S', 'L', 'R']
    queue.append([start, ''])
    visited.add(start)

    while queue:
        cur, oper = queue.popleft()
        visited.add(cur)

        for i, num in enumerate([findD(cur), findS(cur), findL(cur), findR(cur)]):
            if num == fin:
                return oper + orders[i]
        
            if num not in visited:
                queue.append([num, oper + orders[i]])

for _ in range(int(input())):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    print(BFS(num1, num2))

    

    '''# 최종 출력 - 역추적
    output_str = []
    now = num2
    while now != num1:
        if findD(visited[now]) == now:
            output_str.append('D')
        
        elif findS(visited[now]) == now:
            output_str.append('S')

        elif findL(visited[now]) == now:
            output_str.append('L')

        elif findR(visited[now]) == now:
            output_str.append('R')
        
        now = visited[now]

    output_str.reverse()
    print(''.join(output_str))'''