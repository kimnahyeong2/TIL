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
