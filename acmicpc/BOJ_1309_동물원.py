# 문제 푸는 날짜: 220314
# BOJ 1309번 동물원
# # 분류: DP
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1309
# 문제 풀이 핵심: 

N = int(input())
last_cage = []
last_cage.append([1, 1, 1])

for i in range(2, N+1):
    # a: n-1번째 칸이 둘다 빈 경우의 수 / b: 왼쪽에 사자가 들어있는 경우 / c: 오른쪽에 들어있는 경우
    a = (sum(last_cage[-1])) % 9901
    b = (last_cage[-1][0] + last_cage[-1][2]) % 9901
    c = (last_cage[-1][0] + last_cage[-1][1]) % 9901

    last_cage.append([a, b, c])


print(sum(last_cage[-1]) % 9901)