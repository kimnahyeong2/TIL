#뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램 작성
# 뒤집은 소수를 출력해야하고 입력된 순서대로 출력되어야 한다
# 첫자리부터 연속된 0은 무시한다 (예)910을 뒤집으면 019이지만 19로 취급한다
# 뒤집는 함수 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성
# 첫줄에 자연수의 개수 N이 주어지고 그 다음 줄에 N개의 자연수가 주어짐
# 자연수의 크기는 100,000을 넘지 않아야하고 N의 범위는 3보다 크거나 같고 100보다 작거나 같은 수

# @ 나의 문제해결
# @@ 오류 발생 원인 - 너무 꼬아서 생각해 문제를 해결할 수 없었음 (2021.10.25)

def reverse(x):
    value = 0
    while x>0:
        y = x%10
        value = value*10 + y
        x = x//10
    return value

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def main():
    n = int(input())
    n_list = [int(i) for i in input().split()]
    
    for a in n_list:
        tmp = reverse(a)
        
        if isPrime(tmp)==True:
            print(tmp, end=' ')
main()

"""
@ 다른 해결방식 @ --> 나의 문제해결 방식과 90% 이상 같음!
def reverse(x):
    res = 0
    while x>0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)

    if isPrime(tmp):
        print(tmp, end=' ')
"""