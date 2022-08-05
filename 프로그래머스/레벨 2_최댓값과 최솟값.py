# 프로그래머스_레벨 2_최댓값과 최솟값
# 220805

def solution(s):
    nums = list(map(int, s.split()))
    nums.sort()
    return str(nums[0]) + ' ' + str(nums[-1])