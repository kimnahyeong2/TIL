# 임의의 N개의 숫자가 입력으로 주어짐
# N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
# 이분 검색으로 M이 정렬된 상태에서 몇번째에 있는지 구하는 프로그램 작성
# 단 중복값은 존재하지 않음
# 첫줄에 자연수 N과 M이 주어짐
# 두번째 줄에 N개의 수가 공백을 사이에 두고 주어짐
# 첫 줄에 정렬 후 M의 값의 위치 번호를 출력

# 8 32
# 23 87 65 12 57 32 99 81
# 출력 3

N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt) // 2
    if a[mid] == M:
        print(mid + 1)
        break
    elif a[mid] > M:
        rt = mid - 1
    else:
        lt = mid + 1
