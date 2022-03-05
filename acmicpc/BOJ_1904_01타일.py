# 문제 푸는 날짜: 220305
# BOJ 1904번 01타일
# 분류: DP
# 난이도: 실버 3
# https://www.acmicpc.net/problem/1904
# 문제 풀이 핵심: 규칙성 찾기 - 사실은 피보나치??

# 입력받고 리스트 초기값 설정
N = int(input())
blo_list = [0] * (N+2)
blo_list[1] = 1; blo_list[2] = 2

for i in range(1, N-1): blo_list[i+2] = (blo_list[i+1] + blo_list[i]) % 15746

print(blo_list[N])