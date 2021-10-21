# 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다.
# 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다.
# 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
# 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력된다.

n, k = map(int, input().split())
num_list = [int(n) for n in input().split()]

def maxsum():
    num_list.sort()
    num_list.reverse()

    list_sum = []

    for i in range(len(num_list)-2):
        for j in range(i+2,len(num_list)):
            a = sum(num_list[i:i+2],num_list[j])
            list_sum.append(a)
    """
    print(num_list)
    print(list_sum)
    """
    list_sum.sort()
    list_sum.reverse()
    print(list_sum[k-1])

maxsum()