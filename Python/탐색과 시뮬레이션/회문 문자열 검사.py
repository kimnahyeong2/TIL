# N개의 문자열 데이터를 입력받아
# 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우 (회문 문자열)이면 YES출력
# 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성
# 단 회문을 검사할 때 대소문자를 구분하지 않는다

# 첫줄에 정수 N이 주어지고, 그 다음줄부터 N개의 단어가 입력된다
# 각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력
import sys

N = int(input())
N_list = []

for i in range(N):
    N_list.append(input().lower()) #대문자를 소문자로
cnt = 1
for a in N_list:
    re_a = "".join(reversed(a)) #reverse와 reversed의 차이

    if a == re_a:
        print("#",cnt," YES")
    else:
        print("#",cnt," NO")
    cnt += 1
"""
@ 다른 해결방식 1 @
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() #모두 대문자로
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]: #맨마지막위치를 s[-1]로 출력이 가능
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
"""
"""
@ 다른 해결방식 2 @
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() #모두 대문자로
    if s==s[::-1]: # [::-1] 문자를 거꾸로 만들어줌
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
"""