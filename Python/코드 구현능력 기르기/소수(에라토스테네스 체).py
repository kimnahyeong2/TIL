# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램 작성
# 제한시간은 1초입니다!!
#에라토스테네스의 체 이용해서 구하기
"""
에라토스테네스의 체 알고리즘
- 다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대표적인 알고리즘
- N보다 작거나 같은 모든 소수를 찾을 때 사용한다
- 동작과정
    - 2부터 N까지의 모든 자연수를 나열한다
    - 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
    - 남은 수 중에서 i의 배수를 모두 제거한다(단, i는 제거하지 않음)
    - 더 이상 반복할 수 없을 때까지 위의 두 과정을 반복한다
- 시간복잡도는 O(NloglogN)이다
- 다수의 소수를 찾아야 하는 문제에서 효과적으로 사용될 수 있다
- 하지만 소수 여부를 저장해야 하므로 메모리가 많이 필요하다
"""

import time
import datetime

n = int(input())
start = time.time()
num_list = [True] * (n+1)
sum=0
value=[]
#소수라면 true. 소수가 아니라면 false으로 값 넣어주기
for i in range(2,n+1):
    if num_list[i]==True:
        sum = sum+1
        value.append(i)
        for k in range(i,n+1,i):
            num_list[k]=False
print(sum)
end = time.time()
print(f"{end-start:.05f}sec")