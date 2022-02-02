# 문제 푸는 날짜: 220131
# BOJ 1107번 리모컨
# 분류: 재귀?
# 난이도: 골드 5 
# https://www.acmicpc.net/problem/1107
# 문제 핵심: 재귀임을 알아채기, 그리고 재귀함수 잘 구현하기


def listToInt(integers):
    strings = [str(integer) for integer in integers]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

def cnt(num):
    return len(str(num)) + abs(num-target_num)

def createSmallestNum(num, confirm):
    list_temp = []
    if confirm:
        for i in range(len(str(num))):
            list_temp.append(int(str(num)[i]))            

    if [i for i in buttons_able if i > int(str(target_num)[confirm])]:
        list_temp.append(min([i for i in buttons_able if i > int(str(target_num)[confirm])]))
    else:
        return

    while(len(list_temp) < len(str(target_num))):
        list_temp.append(min(buttons_able))
    list_num.append(listToInt(list_temp))

    return

def createBiggestNum(num, confirm):
    list_temp = []
    if confirm:
        for i in range(len(str(num))):
            list_temp.append(int(str(num)[i]))     

    if [i for i in buttons_able if i < int(str(target_num)[confirm])]:
        list_temp.append(max([i for i in buttons_able if i < int(str(target_num)[confirm])]))
    else:
        return


    while(len(list_temp) < len(str(target_num))):
        list_temp.append(max(buttons_able))

    list_num.append(listToInt(list_temp))

    return

def findList(num, confirm):
    if num == target_num and confirm == len(str(num)):
        list_num.append(num)
        return

    createBiggestNum(num, confirm)

    if int(str(target_num)[confirm]) in buttons_able:
        findList(int(str(target_num)[0:confirm+1]), confirm + 1)
        
    createSmallestNum(num, confirm)

def findOther():
    if not buttons_able: return

    num1 = ''
    num2 = ''
    if len(str(target_num)) > 1:
        for _ in range(len(str(target_num)) - 1):
            num1 += str(max(buttons_able))
        
    for _ in range(len(str(target_num)) + 1):
        if (not num2) and list(set(buttons_able) - set([0])):
            num2 += str(min(list(set(buttons_able) - set([0]))))
        else: num2 += str(min(buttons_able))

    if num1 != '': list_num.append(int(num1))
    if num2 != '': list_num.append(int(num2))

target_num = int(input())
broken_buttons_num = int(input())
broken_buttons = []

if broken_buttons_num == 0:
    buttons_able = list(range(0, 10))
else: 
    broken_buttons = list(map(int, input().split()))
    buttons_able = list(set(list(range(0, 10))) - set(broken_buttons))

min_so_far = cnt(100) - 3
list_num = []

findList(0, 0)
findOther()

if list_num:
    print(min(min_so_far, min(map(cnt, list_num))))
else: print(min_so_far)