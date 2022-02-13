# 문제 푸는 날짜: 220213
# BOJ 1676번 팩토리얼 0의 개수
# 분류: 수학/문자열
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1676
# 문제 풀이 핵심: 문자열 인덱싱?

num = int(input())
mult = 1
index = -1

# N! 계산
for i in range(1, num + 1):
    mult *= i

mult = str(mult)

# N!의 0 갯수 계산
while True:
    if mult[index] != '0':
        break

    else: 
        index -= 1

# 출력
print(-index-1)