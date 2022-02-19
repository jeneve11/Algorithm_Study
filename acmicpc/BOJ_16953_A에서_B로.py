# 문제 푸는 날짜: 220218
# BOJ 16953번 A -> B
# 분류: 그리디
# 난이도: 실버 1
# https://www.acmicpc.net/problem/16953
# 문제 풀이 핵심: 

A, B = map(int, input().split())
cnt = 1

while A < B:
    # B의 1의 자리 수가 1일 때 - 맨 끝의 1을 없앤다
    if B % 10 == 1:
        cnt += 1
        B = int(str(B)[:-1])

    # B가 2의 배수일 때 - 2로 나눈다
    elif B % 2 == 0:
        B //= 2
        cnt += 1

    # B가 1도, 짝수도 아니라면 - 루프 탈출
    else: break

# 출력
if A == B: print(cnt)
else: print(-1)