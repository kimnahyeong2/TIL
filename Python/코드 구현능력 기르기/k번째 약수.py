# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수 출력하기
n,k = map(int, input().split())

num_list = []

def num():
    for i in range(1,n+1):
        if n%i==0:
            num_list.append(i)
    if k>len(num_list):
        print(-1)
    else:
        print(num_list[k-1])
num()
