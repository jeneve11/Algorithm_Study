# 문제 푸는 날짜: 220209
# BOJ 1764번 듣보잡
# 분류: 문자열
# 난이도: 실버 4
# https://www.acmicpc.net/problem/1764
# 문제 풀이 핵심: 딕셔너리를 이용한 힙

from collections import defaultdict
import sys

dict_hear = defaultdict(int)
list_overlapped = []
len_hear, len_see = map(int, input().split())
overlapped = 0

# 듣도 못한 사람들을 dictionary에 등록
for i in range(len_hear):
    dict_hear[sys.stdin.readline().rstrip()] = 1

# 보도 못한 사람들 목록을 받아, 만약 dictionary에 이미 등록되어 있다면(듣도 못한 사람이기도 하다면), if문으로 처리
for i in range(len_see):
    temp_name = sys.stdin.readline().rstrip()
    # 듣보잡이라면, overlapped 카운트하고, list_overlapped에 이름을 추가
    if dict_hear[temp_name]:
        overlapped += 1
        list_overlapped.append(temp_name)

# 사전순 정렬
list_overlapped.sort()

# 최종 아웃풋 출력
print(overlapped)
for names in list_overlapped:
    print(names)