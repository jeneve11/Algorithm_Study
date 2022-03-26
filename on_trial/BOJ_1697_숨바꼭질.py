# 문제 푸는 날짜: 220325
# BOJ 1697번 숨바꼭질
# 분류: 
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1697
# 문제 풀이 핵심: 

start, goal = map(int, input().split())
cnt = 0

if start >= goal:
    cnt = start - goal
    print(cnt)

else:
    while 2 * start < goal:
        start *= 2
        cnt += 1
        

    temp = list(str(bin(abs(goal - start * 2))))
    temp.reverse()
    temp = temp[:-2]
    temp_cnt = 1

    for i in range(len(temp)):
        if temp[i] == '1' and i <= cnt + 1: temp_cnt += 1
        elif temp[i] == '1' and i > cnt + 1: temp_cnt += 2

    print(temp)
    print(cnt + min(abs(goal - start), temp_cnt))
    print(cnt, abs(goal - start), temp_cnt)