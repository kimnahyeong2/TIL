# 오름차순으로 정렬이 된 두 리스트가 주어지면
# 두 리스트를 오름차순으로 합쳐 출력하는 프로그램 작성

# 첫번째 줄 : 첫번째 리스트의 크기 N이 주어짐
# 두번째 줄 : N개의 리스트 원소가 오름차순으로 주어짐
# 세번째 줄 : 두번째 리스트의 크기 M이 주어짐
# 네번째 줄 : M개의 리스트 원소가 오름차순으로 주어짐
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않음

# 오름차순으로 정렬된 리스트 출력

N = int(input())
N_list = [n for n in map(int, input().split())]
M = int(input())
M_list = [m for m in map(int, input().split())]

total_list = N_list + M_list
total_list.sort()
print(*total_list)

"""
@ 다른 해결방식 @
# sort를 사용하면 시간복잡도가 NlogN이 됨. 효율성이 떨어지므로 다른 방법을 사용!
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 =0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
for x in c:
    print(x, end=' ')
"""