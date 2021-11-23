# N개의 수로 된 수열 A[1], A[2],--,A[N]이 있다
# 이 수열의 i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램 작성

# 첫째줄 : N과 M이 주어진다
# 둘째줄 : A[1], A[2], --, A[N]이 공백으로 분리되어 주어진다 (30,000을 넘지 않음)

# 경우의 수 출력하기
# 입력
# 8 3
# 1 2 1 3 1 1 1 2
# 출력
# 5

N, M = map(int, input().split())
A = [n for n in map(int, input().split())] #A[0]부터 A[N-1]
cnt = 0
sum = 0

for i in range(N):
    sum = A[i]
    if A[i] == M:
        cnt +=1
        #print("여기서", A[i])
    elif A[i] < M:
        sum = A[i]
        for j in range(i+1,N):
            if sum + A[j] == M:
                cnt += 1
                sum = sum + A[j]
                #print("저기서", sum, A[i], A[j])
                break
            elif sum + A[j] < M:
                sum = sum + A[j]
            else:
                break            
    else:
        pass

print(cnt)

"""
@ 다른 해결방식 @
n, m = map(int, input().split())
a = list(map(int, input().split()))3
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
"""