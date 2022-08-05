# 프로그래머스_레벨 2_N개의 최소공배수
# 220805

def gcd(num1, num2):
    # num1 >= num2임을 보장하기 위해 swap
    if num1 < num2: num1, num2 = num2, num1
    
    while True:
        num1 %= num2
        if num1 == 0: return num2
        else: num1, num2 = num2, num1


def solution(arr):
    # arr에 하나의 요소만 있을 경우, 그 요소를 그대로 반환
    if len(arr) == 1: return arr[0]
    
    # 두 수의 최소공배수 == 두 수의 곱 / 두 수의 최대공약수라는 점을 이용
    ret = arr[0]
    for i in range(1, len(arr)): ret = (ret * arr[i]) / gcd(ret, arr[i])
    
    return ret