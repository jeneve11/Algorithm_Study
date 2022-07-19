# 프로그래머스_레벨 2_하노이의 탑
# 220719

list_a = []

def solution(n):
    hanoi(n, 1, 3)
    return list_a

def hanoi(n, a, b):
    # 탈출 조건
    if n == 1:
        list_a.append([a, b])
        return

    # c는 (1, 2, 3) 중 a, b가 아닌 다른 수 
    for i in range(1, 4):
        if i != a and i != b:
            c = i
            break
    
    hanoi(n-1, a, c)
    list_a.append([a, b])
    hanoi(n-1, c, b)