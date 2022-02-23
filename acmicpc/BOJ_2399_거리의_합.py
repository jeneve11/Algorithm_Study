# 문제 푸는 날짜: 220223
# BOJ 2399번 거리의 합
# 분류: 수학
# 난이도: 브론즈 2
# https://www.acmicpc.net/problem/2399
# 문제 풀이 핵심: 파이썬에선 N^2으로는 안 돌아간다~

sum_diff = []
length = int(input())
nums = [int(x) for x in input().split()]
nums.sort()

len_nums = len(nums)
right_nums = sum(nums)
left_nums = 0

for i, v in enumerate(nums):
    sum_diff.append((right_nums - len_nums * v) + (v * i - left_nums))
    len_nums -= 1
    right_nums -= v
    left_nums += v

print(sum(sum_diff))