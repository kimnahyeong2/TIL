"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
소수가 되는 경우의 개수를 return 하도록solution 함수를 완성해주세요."""

from itertools import combinations
def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):# math를 사용하지 않고 (num//2)+1 까지로 설정
            if num%n == 0:
                return False
        
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))# nums배열을 3개씩 조합 후 list로 변경
    for arr in cmb:
        if is_prime_number(sum(arr)):# cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
            answer += 1 # return 값이 True이면 count(=answer) +1
    
    return answer