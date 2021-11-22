# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 
# 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
# 5자리 회문수의 개수를 출력

N_list = [[int(x) for x in input().split()] for _ in range(7)]
cnt = 0
a = b = 0

for i in range(7):
    for _ in range(3):
        s_num = [n[i] for n in N_list]
        s_num = s_num[a:a+5]
        re_num = list(reversed(s_num))
        #print(s_num, re_num)
        if s_num == re_num:
            cnt += 1
        a += 1

        r_num = N_list[i]
        r_num = r_num[b:b+5]
        ve_num = list(reversed(r_num))
        if ve_num == r_num:
            cnt += 1
        b += 1
    a = b = 0
print(cnt)