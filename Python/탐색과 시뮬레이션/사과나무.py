# 농장은 N*N 격자판으로 이루어져 있으며, N의 크기는 항상 홀수
# 다이아몬드 모양의 격자판만 수확하고 나머지는 남겨놓는다
# 첫 번째 줄에 자연수 N이 주어짐
# 두 번째 줄부터는 각 줄에 N개의 자연수가 주어짐
# 출력 : 수확한 사과의 총 개수 구하기

N = int(input())
N_list = [[int(x) for x in input().split()] for _ in range(N)]

start = stop = arr = N//2
apple = 0

for i in range(N):
    for j in range(start, stop+1):
        apple += N_list[i][j]
    if i < arr:
        start -= 1
        stop += 1
    else:
        start += 1
        stop -= 1
print(apple)

"""
@ 다른 해결방식 @
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
"""