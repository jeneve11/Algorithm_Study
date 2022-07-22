# 프로그래머스_레벨 2_올바른 괄호
# 220722

def solution(s):
    stack = []
    
    # stack 개념 이용하여 ()가 생기는 순간 pop
    # try-except문 사용한 이유: list index 런타임 에러 예방
    for i in s:
        stack.append(i)
        try:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop(); stack.pop()
        except: pass
                
    return False if stack else True