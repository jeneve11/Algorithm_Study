# 문제 푸는 날짜: 220213
# BOJ 6064번 카잉 달력
# 분류: 수학
# 난이도: 실버 1
# https://www.acmicpc.net/problem/6064
# 문제 풀이 핵심: 유클리드 호제법

import sys

# 유클리드 호제법 이용하여 최소공배수 알아내기
def getLCM(num1, num2):
    mult = num1 * num2

    # swap
    if num1 < num2:
        num1, num2 = num2, num1

    while num2:
        rest = num1 % num2
        num1 = num2
        num2 = rest

    return int(mult/num1)



for _ in range(int(input())):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())

    if x == M: x = 0
    if y == N: y = 0

    LCM = getLCM(M, N)
    value = -1

    if M >= N:
        for i in range(y, LCM + 1, N):
            # <x:y>에 의해 표현되는 해를 찾았을 때, i 출력 후 루프 탈출
            if i % M == x:
                value = i
                break
    
    else:
        for i in range(x, LCM + 1, M):
            # <x:y>에 의해 표현되는 해를 찾았을 때, i 출력 후 루프 탈출
            if i % N == y:
                value = i
                break

    print(value)