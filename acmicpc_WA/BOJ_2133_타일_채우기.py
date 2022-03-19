# 문제 푸는 날짜: 220319
# BOJ 2133번 타일 채우기
# 분류: DP
# 난이도: 골드 5
# https://www.acmicpc.net/problem/2133
# 문제 풀이 핵심: 

n = int(input())

ans_list = [0] * 31
ans_list[2] = 3
ans_list[4] = 11

for i in range(5, len(ans_list)):
    if i % 2 == 1: continue

    prev_4 = ans_list[i-4]
    prev_2 = ans_list[i-2]
    ans_list[i] = prev_2 * 3 + prev_4 * 2

print(ans_list)
print(ans_list[n])