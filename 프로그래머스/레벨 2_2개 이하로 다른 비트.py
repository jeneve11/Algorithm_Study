# 프로그래머스_레벨 2_2개 이하로 다른 비트
# 220812

def func(num):
    ret = 0

    num_list = list(bin(num))[2:]
    if num_list[0] == '1': num_list = ['0'] + num_list
    
    # 0과 1의 위치 index를 담는 2개의 list 선언 및 정보 저장 + str to int 형변환
    idx_0 = []; idx_1 = []
    for i in range(len(num_list)):
        if num_list[i] == '1':
            idx_1.append(i)
            num_list[i] = 1
        elif num_list[i] == '0':
            idx_0.append(i)
            num_list[i] = 0
    
    # 가장 마지막 0을 1로 바꿔주고
    num_list[idx_0[-1]] = 1

    # 그 다음으로 보이는 1을 0으로 변환, 없음 말구
    try: num_list[min([x for x in idx_1 if x > idx_0[-1]])] = 0
    except: pass
    
    # 2진법 숫자가 담겨진 list를 10진법 숫자로 변환
    i = 0
    while num_list:
        ret += (num_list.pop()) * (2 ** i)
        i += 1
    
    return ret

def solution(numbers):    
    answer = []
    for number in numbers: answer.append(func(number))
    return answer