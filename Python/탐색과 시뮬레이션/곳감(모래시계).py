# N*N의 격자판으로 이루어진 마당에 감을 말리고 있음
# 해의 위치에 따라 특정위치의 감은 잘 마르지 않아
# 격자의 행을 기준으로 왼쪽 혹은 오른쪽으로 회전시켜 위치를 변경
# 만약 회전명령 정보가 2 0 3 이면 2번째 행을 왼쪽으로 3만큼 회전
# 첫번째 수는 행번호, 두번째 수는 방향(0이면 왼쪽, 1이면 오른쪽), 세번째 수는 회전하는 격자의 수
# M개의 회전명령을 실행한 후 모래시계 모양의 영역에는 감이 총 몇개 있는 지 출력

# 첫 줄에 자연수 N이 주어짐 (홀수이며 3이상 20이하)
# N줄에 걸쳐 각 줄에 N개의 자연수가 주어짐
# 그 다음줄에 회전명령의 개수인 M(1<=M<=10)
# 그 다움줄에는 M개의 회전명령 정보가 M줄에 걸쳐 주어짐
# 출력 : 총 감의 개수를 출력
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""

N = int(input())
N_list = [[int(x) for x in input().split()] for _ in range(N)]
M = int(input())
M_list = [[int(x) for x in input().split()] for _ in range(M)]

for x, y, z in M_list:
    if y == 0:
        for _ in range(z):
            N_list[x-1].append(N_list[x-1].pop(0))
    else:
        for _ in range(z):
            N_list[x-1].insert(0, N_list[x-1].pop())

arr = N//2
start = 0
stop = N
rka = 0

for i in range(N):
    for j in range(start, stop):
        rka += N_list[i][j]
    if i<arr:
        start += 1
        stop -= 1
    else:
        start -= 1
        stop += 1

print(rka)