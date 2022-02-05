# 문제 푸는 날짜: 220202
# BOJ 11723번 집합
# 분류: ?
# 난이도: 실버 5 
# https://www.acmicpc.net/problem/11723
# 문제 풀이 핵심: 메모리 아끼기 - 비트 연산

import sys

numbers_set = set()

# command_list에 명령어, num_list에 숫자 넣기
for i in range(int(input())):
    input_str = sys.stdin.readline().rstrip()
    # 숫자가 붙지 않는 all, empty 명령어 case 처리
    if input_str == 'all':
        for j in range(1, 21):
            numbers_set.add(j)

    elif input_str == 'empty':
        numbers_set.clear()
    
    # 나머지 명령어 case 처리
    else:
        str, num = input_str.split()
        num = int(num)

        if str == 'add':
            numbers_set.add(num)
    
        elif str == 'remove':
            numbers_set.discard(num)

        elif str == 'toggle':
            if num in numbers_set:
                numbers_set.remove(num)
            else:
                numbers_set.add(num)
        
        elif str == 'check':
            if num in numbers_set:
                print(1)
            else:
                print(0)