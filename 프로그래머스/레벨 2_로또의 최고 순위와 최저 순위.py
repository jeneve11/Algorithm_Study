# 프로그래머스_레벨 1_로또의 최고 순위와 최저 순위
# 220720

def solution(lottos, win_nums):
    zeroes = lottos.count(0)
    cnt = 0
    answer_1 = []
    answer_2 = []
    
    for i, win_num in enumerate(win_nums):
        for j, lotto_num in enumerate(lottos):
            if win_num == lotto_num:
                cnt += 1
                answer_1.append(j)
                answer_2.append(i)
    print(answer_1, answer_2, cnt)
    answer = [7 - cnt - zeroes, 7 - cnt]
    for i, v in enumerate(answer):
        if v == 7:
            answer[i] = 6
    return answer