# 프로그래머스_레벨 2_수식 최대화
# 220809

# 문제 풀이 핵심
# 피연산자도 3종류니까 경우의 수 6개... 그리고 문자열 길이 상한이 100이면 그냥 완전 탐색으로 해결할 만한 시간이 나올 듯?
# 일단 연산자와 피연산자 list로 각각 나누고 생각하자

from itertools import permutations

def solution(expression):
    ans = []; op = []; num = []; 
    op_code = ['-', '+', '*']

    # expression를 분석하여 연산자와 피연산자를 op와 num이라는 두 list에 저장
    temp = ''
    for i, v in enumerate(expression):
        # 연산자를 만난 경우
        if v in op_code:
            op.append(v)
            num.append(temp)
            temp = ''
        # 숫자를 만난 경우
        else: temp += v
            
    num.append(temp)
    
    # num list내 숫자들을 type 변환 - str to int
    for i, v in enumerate(num): num[i] = int(v)
    
    # itertools.permutations 이용하여 op_code 우선순위 case 6개 분류
    cases = list(permutations(op_code, 3))

    # 각각의 우선순위 case들에 대해 연산한 후 각각의 case 결과값을 ans list에 집어넣기
    for case in cases:
        # shallow copy를 방지하기 위한 (:)
        new_op = op[:]; new_num = num[:]
        
        for oper in case:    
            while True:
                # index 함수는 못 찾을 때 오류를 내므로 except문을 통해서 while문 탈출
                try: a = new_op.index(oper)
                except: break
                
                # 피연산자 2개 소환!
                temp1 = new_num[a]; temp2 = new_num[a+1]
                
                # 연산하고..
                # 이거 그냥 eval로 처리할 수도 있긴 한데, 그냥 정직하게 if..elif 문으로 처리하는 게 더 빠르다고 판단
                if oper == '-':
                    temp3 = temp1 - temp2
                elif oper == '+':
                    temp3 = temp1 + temp2
                elif oper == '*':
                    temp3 = temp1 * temp2
                
                # 연산 결과값을 다시 집어넣고
                new_num[a+1] = temp3

                # 두 list에서 쓸모없는 pop 해준다 - 이게 O(N)이라 좀 그렇긴 한데.. 일단 진행
                new_op.pop(a); new_num.pop(a)
                
        ans.append(abs(new_num[0]))
      
    # ans list 내에서 가장 큰 값을 반환
    return max(ans)