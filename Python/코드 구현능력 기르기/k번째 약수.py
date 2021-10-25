# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수 출력하기

# @ 나의 문제해결
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

"""
@ 다른 해결방식 @
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i==0:
        cnt += 1
    if cnt == k:
        print(k)
        break
else:
    print(-1)

-> 여기서 else구문으로 넘어오는 것은 for문이 끝까지 실행되면서 break를 만나지 않았을 경우 실행이 됨
-> break를 만나면서 for문을 빠져나오는 상태라면 else구문은 실행되지 않음
"""