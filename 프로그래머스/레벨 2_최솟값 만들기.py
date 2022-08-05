# 프로그래머스_레벨 2_최솟값 만들기
# 220804

def solution(A,B):
    answer = 0

    # A는 오름차순, B는 내림차순으로 정렬
    A.sort()
    B.sort(reverse=True)
    
    # 각각 곱하기
    for a, b in zip(A, B):
        answer += (a*b)

    return answer