# 문제 푸는 날짜: 220203
# BOJ 1747번 소수&팰린드롬
# 분류: 수학?
# 난이도: 실버 1 
# https://www.acmicpc.net/problem/1747
# 문제 풀이 핵심: 에라스토테네스의 체

import math

# 숫자가 팰린드롬 수인지 판별하는 함수
def isPalindrome(int_num):
    str_num = str(int_num)
        
    for i in range(len(str_num)):
        j = len(str_num) - i - 1
        if j <= i:
            break

        elif str_num[i] != str_num[j]:
            return False

    return True

num = int(input())
HIGH_LIMIT = 1100000

# 배열 만들고 0, 1 False로 변경(절대 소수가 아니므로)
int_list = [True] * (HIGH_LIMIT)
int_list[0] = False
int_list[1] = False

# 2 ~ root(HIGH_LIMIT)의 배수 제거
for i in range(2, math.ceil(HIGH_LIMIT ** 1/2)):
    for j in range(i*2, HIGH_LIMIT, i):
        int_list[j] = False

# num보다 크거나 같은 소수이며 팰린드롬 수인 가장 작은 수를 출력하고 프로그램 종료
for i, v in enumerate(int_list):
    if i >= num and v and isPalindrome(i):
        print(i)
        exit()