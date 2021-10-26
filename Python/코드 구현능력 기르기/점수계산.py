# OX 문제로 만들어진 시험에서 연속적으로 답이 맞는 경우에는 가산점을 주기로 함
# 1번 문제가 맞는 경우 1점으로 계산
# 답을 틀렸다가 답이 맞을 경우도 1점으로 계산
# 연속적으로 문제의 답이 맞는 경우 2번째는 2점, 3번째는 3점
# 틀린문제는 0점으로 계싼
# 첫번째 줄에 문제의 개수 N이 주어짐
# 두번째 줄에는 N개 문제의 채점 결과를 나타냐는 0 혹은 1이 빈칸을 사이에 두고 주어짐
# 0은 문제의 답이 틀렸을 경우, 1은 문제의 답이 맞는 경우
# 입력에서 주어진 채점 결과에 가산점으 고려한 총 점수를 출력

N = int(input())
N_list = list(map(int, input().split()))
score = 0
bonus = 0
total = 0
for i in range(N-1):
    if(N_list[i]==1):
        score = score + 1
        if(N_list[i+1]==1):
            bonus = bonus + 1
total = score + bonus
print(total)