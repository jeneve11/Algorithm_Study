# 문제 푸는 날짜: 220219
# BOJ 1041번 주사위
# 분류: 구현?
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1041
# 문제 풀이 핵심: 규칙 찾기

dice = int(input())
nums = [int(i) for i in input().split()]

# 예외 처리 - dice가 1인 경우
if dice == 1:
    print(sum(nums) - max(nums))
    exit()


def findMin(nums, side):
    # 임의값 설정 - 50*3보다는 큰 자연수
    temp_min = 151

    # 2면이 노출되는 주사위 case
    if side == 2:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums):
                if i1 == i2 or i1 + i2 == 5:
                    continue
                
                if v1 + v2 < temp_min:
                    temp_min = v1 + v2

    # 3면이 노출되는 주사위 case
    elif side == 3:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums):
                for i3, v3 in enumerate(nums):
                    if i1 == i2 or i2 == i3 or i1 == i3 or i1 + i2 == 5 or i1 + i3 == 5 or i2 + i3 == 5:
                        continue

                    if v1 + v2 + v3 < temp_min:
                        temp_min = v1 + v2 + v3

    return temp_min


side_1 = min(nums) * ( 5*((dice-2)**2) + 4*(dice-2) )
side_2 = (2 * dice - 3) * 4 * findMin(nums, 2)
side_3 = 4 * findMin(nums, 3)

print(side_1 + side_2 + side_3)