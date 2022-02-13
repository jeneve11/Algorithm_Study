# 문제 푸는 날짜: 220213
# BOJ 2609번 최대공약수와 최소공배수
# 분류: 수학
# 난이도: 실버 5
# https://www.acmicpc.net/problem/2609
# 문제 풀이 핵심: 유클리드 알고리즘

num1, num2 = map(int, input().split())
mult = num1 * num2

# swap
if num1 < num2:
    num1, num2 = num2, num1

while num2:
    rest = num1 % num2
    num1 = num2
    num2 = rest

print(num1)
print(int(mult/num1))