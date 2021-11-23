# 문자와 숫자가 섞여있는 문자열이 주어지면
# 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다
# 만들어진 자연수와 그 자연수의 개수를 출력
# 단, 첫자리가 0일 경우에는 자연수화 할 때 무시한다

# 첫줄에 숫자가 적힌 문자열이 주어진다. (문자의 길이는 50을 넘지 않음)
# 첫줄에 자연수를 출력하고 두번째 줄에 약수의 개수를 출력한다

#g0en2Ts8eSoft 28 6
import re

S = input()
N = re.sub(r'[^0-9]','',S) #0-9를 제외한 문자를 제거
num = int(N) #숫자를 int형으로 변경
cnt = 0

for i in range(1, num+1):
    if num%i==0:
        cnt += 1

print(num)
print(cnt)

"""
@ 다른 해결방식 @
s = input()
res = 0
for x in s:
    if x.isdecimal(): # .isdecimal() : 0부터 9의 수를 찾아줌 .isdigit() : 모든 숫자형태를 찾아줌
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
"""