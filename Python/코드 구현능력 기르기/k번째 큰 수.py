# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다.
# 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다.
# 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
# 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.

# @ 나의 문제해결
# @@ 오류 발생 원인 - 중복된 값 제거를 해주지 않음 (2021.10.25)
n, k = map(int, input().split())
num_list = [int(n) for n in input().split()]

def maxsum():

    list_sum = []

    for i in range(0, n-2):
        for j in range(i+1,n-1):
            b = num_list[i] + num_list[j]
            for e in range(j+1, n):
                a = b + num_list[e]
                list_sum.append(a)
    result = list(set(list_sum))
    result.sort()
    result.reverse()
    #print(result)
    print(result[k-1])

maxsum()

"""
@ 다른 해결방식 @
"""