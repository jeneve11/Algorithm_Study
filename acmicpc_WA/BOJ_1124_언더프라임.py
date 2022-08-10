# 문제 푸는 날짜: 220808
# BOJ 1124번 언더프라임
# 분류: 
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1124
# 문제 풀이 핵심: 

import math

# 에라스토테네스의 체 - 일정 구간 내의 모든 소수를 찾는 방법
def getPrimeList(num):
    prime_list = [False, False] + [True] * (num-1)
    for i in range(2, math.ceil(num ** (1/2))):
        if prime_list[i]:
            for j in range(2*i, num+1, i):
                prime_list[j] = False
    return [i for i, v in enumerate(prime_list) if v]

a, b = map(int, input().split())
num_list = list(range(a, b+1))

prime_list = getPrimeList(b)

print(num_list)
print(prime_list)
