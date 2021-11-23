# 지도 정보가 N*N 격자판에 주어집니다.
# 각 격자에는 그 지역의 높이가 쓰여있습니다.
# 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요. 
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.
# 0 0 0 0 0 0 0
# 0 5 3 7 2 3 0
# 0 3 7 1 6 1 0
# 0 7 2 5 3 4 0
# 0 4 3 6 4 1 0
# 0 8 7 3 5 2 0
# 0 0 0 0 0 0 0
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 
# 각 자연수는 100을 넘지 않는다.

N = int(input())
N_list = [[int(0)]*(N+2) for i in range(N+2)]
num_list = [[int(x) for x in input().split()] for _ in range(N)]

for a in range(1,N+1):
    for b in range(1, N+1):
        N_list[a][b] = num_list[a-1][b-1]
#print(N_list)

cnt = 0

for k in range(1, N+1):
    for s in range(1, N+1):
            if N_list[k][s] > N_list[k-1][s]:
                if N_list[k][s] > N_list[k+1][s]:
                    if N_list[k][s] > N_list[k][s-1]:
                        if N_list[k][s] > N_list[k][s+1]:
                            cnt += 1
print(cnt)

"""
@ 다른 해결방식 @
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n) # 0번행에 0으로 이루어진 일차원 리스트 삽입
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): # all() 모든 조건을 만족할 때에
            cnt += 1
print(cnt)
"""