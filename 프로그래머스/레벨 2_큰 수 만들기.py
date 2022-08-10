# 프로그래머스_레벨 2_큰 수 만들기
# 220804
# 핵심 개념: 스택(LIFO)

def solution(number, k):
    num_list = [int(i) for i in list(number)]
    answer = []
    
    # num_list의 값을 하나하나 answer에 append
    # 단, answer[-1]보다 큰 값이 들어오면 계속 pop
    for num in num_list:
        while True:
            if not answer or k == 0 or num <= answer[-1]: break
            if k > 0 and num > answer[-1]:
                answer.pop()
                k -= 1
        
        answer.append(num)
    
    ret = ''.join([str(x) for x in answer[:(len(number)-k)]])
    
    return ret