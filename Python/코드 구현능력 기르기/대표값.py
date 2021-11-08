# N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
# 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
# 첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연수가 주어집니다.
# 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

# @ 나의 문제해결
def student_score():
    n = int(input())
    score_list = [int(n) for n in input().split()] #입력하는 숫자를 배열에 공백을 기준으로 나누어 집어넣어주기
    avg = round(sum(score_list)/n) #round 사용해 소수점 첫째자리에서 반올림
    min = 100

    for idex,value in enumerate(score_list): #enumerate 리스트값의 인데스와 값을 동시에 가져올 수 있게 해줌
        tmp = abs(avg-value)
        if tmp<min:
            min = tmp
            best = idex+1
            score = value
        elif tmp==min:
            if value>score:
                score = value
                best = idex+1
    print(avg, best)

student_score()
"""
@ 다른 해결방식 @ --> 나의 문제해결 방식과 유사!
n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a)/n)
# round함수는 round_half_even 방식 (4.500일 경우 짝수쪽으로 감->4)
# 0.5를 더해 값을 변경해주는 방식으로 사용하는 것이 좋음
ave = (sum(a)/n) + 0.5
ave = int(ave)

min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x>score:
            score = x
            res = index + 1
print(ave, res)

"""