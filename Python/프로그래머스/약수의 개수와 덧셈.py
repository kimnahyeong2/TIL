# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return
def solution(left, right):
    answer = 0
    count = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                count += 1
        if count % 2 == 1:
            i = -i
        answer += i
        count=0
    return answer