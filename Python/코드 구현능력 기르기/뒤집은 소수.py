#뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램 작성
# 뒤집은 소수를 출력해야하고 입력된 순서대로 출력되어야 한다
# 첫자리부터 연속된 0은 무시한다 (예)910을 뒤집으면 019이지만 19로 취급한다
# 뒤집는 함수 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성
# 첫줄에 자연수의 개수 N이 주어지고 그 다음 줄에 N개의 자연수가 주어짐
# 자연수의 크기는 100,000을 넘지 않아야하고 N의 범위는 3보다 크거나 같고 100보다 작거나 같은 수

def reverse(x):
    k = int(str(x)[::-1]) #요기 다시 공부하기!
    return k

def isPrime(x):
    if x==3:
        return x
    elif x%2!=0 and x%3!=0 and x%5!=0:
        return x
    else:
        return False

def main():
    n = int(input())
    num_list = [int(i) for i in input().split()]
    reverse_num = []
    Prime_num = []

    for i in num_list:
        reverse_num.append(reverse(i))

    for j in reverse_num:
        Prime_num.append(isPrime(j))
    result = [value for index,value in enumerate(Prime_num) if Prime_num[index]!=False]
    print(result)

main()

#main함수 안쓰고 할 수 있는 방법 다시 찾아보기