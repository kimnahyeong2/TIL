# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고
# 그 합이 최대인 자연수를 출력하는 프로그램 작성
# 각 자연수의 자릿수의 합을 구하는 함수는 def digit_sum(x)를 작성해서 프로그래밍하시오.
# 첫줄에 자연수의 개수 N이 주어지고 그 다음 줄에는 N개의 자연수가 주어진다.
# 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력한다.
# @ 나의 문제해결
n = int(input())
cal_list = [int(n) for n in input().split()]
sum_list = []

#각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    sum = 0
    while x>0:
        sum = sum + (x % 10)
        x = x // 10
    sum_list.append(sum)

def main():
    for i in cal_list:
        digit_sum(i)
    k = sum_list.index(max(sum_list))
    print(cal_list[k])

main()

"""
@ 다른 해결방식 @
# 1
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x % 10
        x = x // 10
    return sum
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

# 2
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    for i in str(x): #문자열화 시켜주기
        sum += int(i)
    return sum
       
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
"""