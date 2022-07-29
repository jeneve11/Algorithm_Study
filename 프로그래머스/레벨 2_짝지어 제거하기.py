# 프로그래머스_레벨 2_짝지어 제거하기
# 220724

def solution(s):
    s = list(s)
    stack = []
    
    # list 순회 - 시간복잡도 O(n)
    for i in s:
        # try-except문을 통해 list index 에러 발생 시(배열이 비어있을 시) 그냥 요소 추가
        try:
            # 이전 요소와 같으면 요소 추가하지 않고, 그냥 이전 요소 pop
            if stack[-1] == i:
                stack.pop()
            # 이전 요소와 다르면 그냥 요소 추가
            else: stack.append(i)
            
        except: stack.append(i)
    
    # stack이 비었으면 0, 차 있으면 1 리턴
    return 0 if stack else 1