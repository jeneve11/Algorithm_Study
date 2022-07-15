# 프로그래머스_레벨 1_실패율
# 220715

# 실패율이 제일 높은 N개의 stage를 list에 담아 return
# 같은 애들은 오름차순으로

def solution(N, stages):
    answer = []    
    stage_cnt = []
    lista = [0] * N
    
    # lista에 각 난이도 별 실패율을 계산해서 넣어 줌
    for i in range(1, N+1):
        # 예외 처리 - DivisionByZero case를 생각해 줌
        try: lista[i-1] = stages.count(i)/(len(stages) - sum(stage_cnt))
        except: lista[i-1] = 0
        stage_cnt.append(stages.count(i))
        
    # 실패율이 높은 순서대로 answer list에 삽입
    for i in range(N):
        maxi = -1
        temp = 9999
        for j in range(len(lista)):
            if lista[j] > maxi:
                maxi = lista[j]
                temp = j
                
        lista[temp] = -1
        answer.append(temp+1)
    
    return answer