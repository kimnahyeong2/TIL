# 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 
# 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
# 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요

num_list = [[int(x) for x in input().split()] for _ in range(9)]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def one():
    for i in range(9):
        tmp = sorted(num_list[i])
        if tmp != number:
            return("NO")

def two():
    a = b = 0
    cnt = 0
    for _ in range(9):
        k = [num_list[a][b], num_list[a][b+1], num_list[a][b+2], num_list[a+1][b], num_list[a+1][b+1], num_list[a+1][b+2], num_list[a+2][b], num_list[a+2][b+1], num_list[a+2][b+2]]
        k = sorted(k)
        if k != number:
            return("NO")
        cnt += 1
        if cnt % 3 == 0:
            a += 3
            b = 0
        else:
            b += 3

result = one()
if result == "NO":
    print("NO")
else:
    result = two()
    if result == "NO":
        print("NO")
    else:
        print("YES")
"""
@ 다른 해결방식 @
def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
                if sum(ch3) != 9:
                    return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("Yes")
else:
    print("NO")
"""