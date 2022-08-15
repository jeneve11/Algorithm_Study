# 문제 푸는 날짜: 220814
# BOJ 17626번 Four Squares
# 분류: 완전 탐색
# 난이도: 실버 3
# https://www.acmicpc.net/problem/17626
# 문제 풀이 핵심: ?

from itertools import combinations

num = int(input())
nums_list = [0] * (num + 1)
square_nums = []

# 제곱수 list 생성
i = 1
while (i ** 2) <= num:
    square_nums.append(i ** 2)
    nums_list[i**2] += 1
    i += 1

print(nums_list)

# 1개로 표현
if num in square_nums:
    print(1)
    exit()

# 2개로 표현
two_nums = list(combinations(square_nums, 2))
two_nums_sum = []
for i in two_nums:
    two_nums_sum.append(sum(i))
    if sum(i) == num:
        print(2)
        exit()

#   print(two_nums_sum)

for i, k in zip(two_nums_sum, two_nums):
    for j in square_nums:
        if i+j == num and j not in k:
            print(3)
            exit()

# 3개로 표현
#for i in list(combinations(square_nums, 3)):
#    if sum(i) == num:
#        print(3)
#        exit()

# 4개로 표현
print(4)