# 1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 한 줄로 놓여있다
# 각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다
# 다음과 같은 규칙으로 카드의 위치를 바꾼다
# 구간[a,b](단 1<=a<=b<=20)가 주어지면 위치 a부터 위치 b까지의 카드를 역순으로 놓는다
# 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 후 마지막 카드들의 배치를 구하는 프로그램을 작성

# 총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다
# i번째 줄에는 i번째 구간의 시작 위치 ai와 끝 위치 bi가 차례대로 주어진다
# 이때 두 값의 범위는 1<= ai <= bi <= 20
# 주어진 10개의 구간 순서대로 뒤집는 작업을 햇을 때, 마지막 카드들의 배치를 한줄에 출력

card_list = [i for i in range(21)]

cnt=0
while cnt<10:
    start, end = map(int, input().split())
    card_list[start:end+1] = card_list[end:start-1:-1]
    cnt += 1
del card_list[0]

print(*card_list) #정수형 리스트를 []와 ,없이 출력하고 싶다면 *을 사용

"""
@ 다른 해결방식 @
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] #스와프
a.pop(0) # pop()은 맨 뒤에서부터 끄집어냄. pop(0)은 맨 앞에 있는걸 끄집어냄
for x in a:
    print(x, end=' ')
"""