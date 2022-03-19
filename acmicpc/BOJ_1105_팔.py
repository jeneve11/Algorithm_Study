# 문제 푸는 날짜: 220317
# BOJ 1105번 팔
# 분류: 그리디 알고리즘
# 난이도: 실버 1
# https://www.acmicpc.net/problem/1105
# 문제 풀이 핵심: 선형시간 알고리즘으로는 해결할 수 없다

# 두 숫자의 공통부분을 추출하는 함수
def findCommon(num1, num2):
    num = str(num1)
    ret = 0
    num1 = str(num1)
    num2 = str(num2)

    while num1 and num1[0] == num2[0]:
        num1 = num1[1:]
        num2 = num2[1:]
        ret += 1

    return num[:ret]


left, right = map(int, input().split())

# 시작 숫자와 끝 숫자 자릿수가 다를 경우 - 10^n 꼴의 숫자가 꼭 끼어있기 때문에 8이 하나도 포함되지 않는 숫자가 존재함
if len(str(left)) != len(str(right)): print(0)

# 시작 숫자와 끝 숫자 자릿수가 같은 경우 - 공통부분의 8 갯수가 답인듯
else: print(findCommon(left, right).count('8'))