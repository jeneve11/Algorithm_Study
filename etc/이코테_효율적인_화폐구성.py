# 문제 푸는 날짜: 220330
# 분류: DP
# 난이도: ??
# https://broship.tistory.com/211
# 문제 풀이 핵심: 

import sys

coins = [] # 동전들을 저장하는 list

# 입력 받기
N, M = map(int, input().split())
for _ in range(N): coins.append(int(input()))
coins.sort() # 동전들을 올림차순으로 정렬

# 해당 index의 값을 만들기 위한 동전의 갯수를 저장하는 list
dp = [sys.maxsize] * (M+1)
dp[0] = 0 # 0번째 index 값을 0으로 초기화

for coin in coins:
    for i, v in enumerate(dp):
        # maxsize가 아닌(즉, 이미 그 값을 얻기 위해 몇개의 동전이 필요한지가 이미 알려진 경우일때)
        if v != sys.maxsize:
            cnt = 0
            for k in range(i, M+1, coin):
                dp[k] = min(dp[k], v + cnt)
                cnt += 1


# 출력
if dp[-1] != sys.maxsize: print(dp[-1])
else: print(-1)