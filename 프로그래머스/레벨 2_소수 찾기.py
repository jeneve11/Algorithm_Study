# 프로그래머스_레벨 2_소수 찾기
# 220719

import math

def solution(numbers):
    answer = 0
    
    # numbers로 구성할 수 있는 가장 큰 함수를 얻어내는 코드
    # ex) numbers='011'일때 max_num은 110이 된다.
    numbers = list(numbers)
    numbers.sort(reverse=True)
    max_num = int(''.join(numbers))
    
    # prime_nums는 2 ~ max_num 구간 내의 모든 소수 list
    prime_nums = getPrimeList(max_num)
    
    # canMade를 통해 해당 구간 소수들 중 numbers로 만들어지는 경우 answer count를 올린다.
    for prime_num in prime_nums:
        if canMade(prime_num, numbers): answer += 1
    
    return answer

# 2 ~ num의 구간에서 소수인 숫자 list를 반환하는 함수
def getPrimeList(num):
    prime_list = [False, False] + [True]*(num-1)
    for i in range(2, math.ceil(num ** (1/2))):
        if prime_list[i]:
            for j in range(2*i, num+1, i):
                prime_list[j] = False
    return [i for i, v in enumerate(prime_list) if v]

# num이 num_list의 숫자들로 구성되어 있는지 여부를 반환하는 함수
def canMade(num, num_list):
    num = list(str(num))
    for i in range(0, 10):
        if num.count(str(i)) > num_list.count(str(i)):
            return False
    return True
