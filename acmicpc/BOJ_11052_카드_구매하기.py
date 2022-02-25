# 문제 푸는 날짜: 220225
# BOJ 11052번 카드 구매하기
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/11052
# 문제 풀이 핵심: 

import sys
sys.setrecursionlimit(10 ** 6)

# n개의 카드를 사는 가장 비싼 가격 반환하는 함수
def findMaxPrice(n):
    # 이미 메모된 것은 바로 반환 후 함수 탈출
    if max_price[n]: return max_price[n]

    # 메모되지 않은 case
    temp_max = price[n]
    for i in range(1, n):
        temp_max = max(temp_max, findMaxPrice(i) + findMaxPrice(n-i))

    # 메모 후 반환
    max_price[n] = temp_max
    return max_price[n]


N = int(input())

price = [0] + [int(x) for x in input().split()]
max_price = [0] * len(price)
max_price[1] = price[1]

print(findMaxPrice(N))