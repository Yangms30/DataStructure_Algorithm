def solution(quiz):
    answer = []
    # 퀴즈는 리스트로 들어오고 한 퀴즈는 string으로 되어 있음
    for q in quiz:
        susik = q.split(' ')
        num1 = int(susik[0])
        s = susik[1]
        num2 = int(susik[2])
        ans = int(susik[4])
        if (s == '-'):
            if num1 - num2 == ans:
                answer.append('O')
            else:
                answer.append('X')
        if (s == '+'):
            if num1 + num2 == ans:
                answer.append('O')
            else:
                answer.append('X')
        
    return answer