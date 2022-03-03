# 문제 푸는 날짜: 220221
# BOJ 24500번 blobblsuh
# 분류: 비트 연산
# 난이도: 실버 2
# https://www.acmicpc.net/problem/24500
# 문제 풀이 핵심: 


N = int(input())

target = ''
for _ in range(len(bin(N)) - 2):
    target += '1'


if '0' not in str(bin(N))[2:]:
    print(1)
    print(N)

else:
    print(2)
    print(int(target, 2) - N)
    print(N)