# N개의 숫자로 이루어진 숫자열 중 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 수
# 첫번째 줄에 테스트 케이스 T(1<=T<=10)
# 각 케이스별 첫 번째 줄의 자연수 N, s, e, k
# 두 번째 줄에는 N개의 숫자가 주어짐

t = int(input())

def case():
    t_list = []
    for i in range(t):
        n, s, e, k = map(int, input().split())
        num_list = [int(n) for n in input().split()]
        del num_list[e:]
        del num_list[:s-1]
        #print(num_list)
        num_list.sort()
        t_list.append(num_list[k-1])
    for j in range(t):
        print("#",j+1,":",t_list[j])
case()
