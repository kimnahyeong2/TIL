# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력
# 첫 줄에 자연수 N (1 <= N <= 50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어짐
# 각 자연수는 100을 넘지 않음
# 최대합을 출력
# 입력예제
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""

N = int(input())
N_list = [[int(x) for x in input().split()] for _ in range(N)]

value_list=[]
value = 0
value1 = 0
value2 = 0

for i in range(len(N_list)):
    for j in range(len(N_list)):
        value += N_list[j][i]
        value1 += N_list[i][j]
    value_list.append(value)
    value_list.append(value1)
    value2 += N_list[i][i]
    value = 0
    value1 = 0
value_list.append(value2)

print(max(value_list))

"""
@ 다른 해결방식 @
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -214700000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)
"""