# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 
# 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
# 첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 
# 그 다음 줄부터 N개의 줄에 사람들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 가장 많은 상금을 받은 사람의 상금을 출력
# @ 나의 문제해결
try:
    N = int(input())

    if N<2 or N>1000:
        raise
except:
    print("참가인원을 다시 설정해주세요")


def prize():
    N_list = list(map(int, input().split()))
    count_dic = {}

    for i in N_list:
        try : count_dic[i] += 1
        except : count_dic[i] = 1

    if len(count_dic) == 3:
        reward = max(N_list)
        reward_value = reward * 100

    elif len(count_dic) == 2:
        reward = max(count_dic, key = count_dic.get)
        reward_value = reward *100 + 1000

    else:
        reward = N_list[0]
        reward_value = reward * 1000 + 10000

    return reward_value

price = []
for i in range(N):
    price.append(prize())

print(max(price))

"""
@ 다른 해결방식 @
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c*100
    if money > res:
        res = money
print(res)
"""