# 문제 푸는 날짜: 220805
# BOJ 7568번 덩치
# 분류: 완전 탐색
# 난이도: 실버 5
# https://www.acmicpc.net/problem/7568
# 문제 풀이 핵심: N의 갯수가 2~50 밖에 안된다고? 걍 다 세버리면(브루트포스) 될듯? 이라고 빠르게 생각하기

N = int(input())

wei, hei, ans = [], [], []

# 몸무게, 체중을 2개의 배열에 나누어 저장
for i in range(N):
    a, b = map(int, input().split())
    wei.append(a)
    hei.append(b)

# i번째 요소보다 몸무게와 체중이 둘다 큰 요소를 찾으면 +1하는 방법으로 모든 요소의 '덩치 등수'를 구한다
# 예상 시간 복잡도 - O(N^2)
for i in range(N):
    this_a, this_b = wei[i], hei[i]
    bigger_cnt = 0
    for j in range(N):
        if this_a < wei[j] and this_b < hei[j]: bigger_cnt += 1

    ans.append(bigger_cnt + 1)

print(*ans)

