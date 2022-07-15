# 프로그래머스_레벨 1_부족한 금액 계산하기
# 220715

def solution(price, money, count):
    for i in range(1, count+1):
        money -= price * i
    
    if money < 0: return -money
    else: return 0