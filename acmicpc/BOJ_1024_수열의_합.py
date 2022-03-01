# 문제 푸는 날짜: 220301
# BOJ 1024번 수열의 합
# 분류: 수학
# 난이도: 실버 2
# https://www.acmicpc.net/problem/1024
# 문제 풀이 핵심: 

N, L = map(int, input().split())

for i in range(L, 101):
    temp_nums = []
    avg = int(N/i)

    # i 홀수 case
    if i % 2 == 1 and N/i == avg:
        temp_nums.append(avg)
        i //= 2 
        for j in range(1, i+1):
            temp_nums.append(avg-j)
            temp_nums.append(avg+j)

    # i 짝수 case
    if i % 2 == 0 and N/i == int(N/i) + 0.5:
        for j in range(1, (i//2)+1):
            temp_nums.append(avg-j+1)
            temp_nums.append(avg+j)

    # 음수를 포함하거나 빈 리스트 case 처리
    if not temp_nums or [x for x in temp_nums if x < 0]:
        continue

    temp_nums.sort()
    print(*temp_nums)
    exit()

print(-1)