# 문제 푸는 날짜: 220217
# BOJ 4948번 베르트랑 공준
# 분류: 수학
# 난이도: 실버 2
# https://www.acmicpc.net/problem/4948
# 문제 풀이 핵심: 에라스토테네스의 체


import math
import sys

# 숫자 데이터 입력받아 list에 집어 넣기
num_list = []
while True:
    num = int(sys.stdin.readline().rstrip())
    if not num: break

    num_list.append(num)

# 에라스토테네스의 체 구현
MAXI = max(num_list) * 2
prime_list = [True] * (MAXI + 1)
prime_list[0], prime_list[1] = False, False

for i in range(2, math.ceil(MAXI**(1/2))):
    for j in range(2*i, MAXI+1, i):
        prime_list[j] = False

# 조건(num < i <= num*2)에 맞는 소수 갯수 출력
for num in num_list:
    print(len([i for i, v in enumerate(prime_list) if v == True and i > num and i <= num*2]))