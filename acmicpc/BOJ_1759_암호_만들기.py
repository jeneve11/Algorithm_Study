# 문제 푸는 날짜: 220302
# BOJ 1759번 암호 만들기
# 분류: 
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1759
# 문제 풀이 핵심: 

import itertools


L, C = map(int, input().split())
letters = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']
answer_list = []

# 조합 이용
combi_list = list(itertools.combinations(letters, L))

for combi in combi_list:
    vowel_cnt = 0; conso_cnt = 0

    # 자음 / 모음 갯수 count
    for i in combi:
        if i in vowels: vowel_cnt += 1
        else: conso_cnt += 1

    # 자음 2개 / 모음 1개 규칙 충족한다면 answer_list에 추가
    if vowel_cnt >= 1 and conso_cnt >= 2:
        combi = list(combi)
        combi.sort()
        temp = ''.join(combi)
        answer_list.append(combi)

# 사전순 정렬 후 출력
answer_list.sort()
for answer in answer_list: print(*answer, sep='')