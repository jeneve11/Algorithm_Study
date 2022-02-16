# 문제 푸는 날짜: 220216
# BOJ 10844번 쉬운 계단 수
# 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/10844
# 문제 풀이 핵심: 점화식

num = int(input())

dp = [0, 9]
val_list = [1] * 10
val_list[0] = 0

for i in range(2, num + 1):
    temp_list = [0] * 10
    for index, value in enumerate(val_list):
        if index == 0:
            temp_list[1] += value
        elif index == 9:
            temp_list[8] += value
        else:
            temp_list[index - 1] += value
            temp_list[index + 1] += value

    
    dp.append(sum(temp_list))

    val_list = temp_list

# 출력
print(dp[num] % 1000000000)