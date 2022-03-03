# 문제 푸는 날짜: 220303
# BOJ 1188번 음식 평론가
# 분류: 
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1188
# 문제 풀이 핵심: 규칙성 찾기

# 유클리드 호제법 이용하여 최대공약수를 구하는 함수
def findGCD(num1, num2):
    # 항상 num1 >= num2를 보장
    if num1 < num2:
        num1, num2 = num2, num1

    while num2:
        rest = num1 % num2
        num1 = num2
        num2 = rest

    return num1

N, M = map(int, input().split())

gcd = findGCD(N, M)
N, M = N//gcd, M//gcd

if (N/M).is_integer(): print(0)
else: print(gcd * (M-1))