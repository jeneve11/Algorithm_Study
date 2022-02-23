# 문제 푸는 날짜: 220223
# BOJ 2108번 통계학
# 분류: 자료 구조
# 난이도: 실버 3
# https://www.acmicpc.net/problem/2108
# 문제 풀이 핵심: dictionary 사용

from collections import defaultdict
import sys

# 입력 받기
num_dict = defaultdict(int)
N = int(input())
for _ in range(N): num_dict[int(sys.stdin.readline().rstrip())] += 1

# 산술평균 출력
sum_nums = sum([v*k for k, v in num_dict.items()])
print(round(sum_nums / sum(num_dict.values())))

# 중앙값 출력
target = int(sum(num_dict.values()) / 2)
for k, v in sorted(num_dict.items()):
    target -= v
    if target < 0:
        print(k)
        break

# 최빈값 출력
freq_value = [k for k, v in num_dict.items() if max(num_dict.values()) == v]
if len(freq_value) == 1: print(*freq_value)
else: print(sorted(freq_value)[1])

# 범위 출력
print(max(num_dict) - min(num_dict))