# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

while True:
    n,m = input().split()
    if n and m in ['4','6','8','12','20']:
        break
    else:
        print("4, 6, 8, 12, 20 중 하나의 값이 입력되어야 합니다. 다시 입력해주세요")
n = int(n)
m = int(m)

def persent():
    sum_list = [0 for i in range((n+m)+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            value = i+j
            sum_list[value] += 1

    #max_list = [index for index, value in enumerate(sum_list) if value == max(sum_list)]
    #print(max_list)

    for index, value in enumerate(sum_list):
        if value == max(sum_list):
            print(index, end=' ')
persent()