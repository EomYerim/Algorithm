# import sys
# input = sys.stdin.readline
# N = int(input())
# num = [int(input()) for _ in range(N)]
# max_length = len(str(max(num)))
# numbers = [str(i).zfill(max_length) for i in num]
# max_count = 0 # 최대 개수 저장

# for i in range(N):
#     valid_set = [numbers[i]] 
#     for j in range(i + 1, N):
#         check = True  # valid_set에 포함될 수 있는지 여부
#         for k in range(max_length):
#             if int(numbers[i][k]) + int(numbers[j][k]) >= 10:
#                 check = False
#                 break
#         if check:
#             valid_set.append(numbers[j])
#     max_count = max(max_count, len(valid_set))

# print(max_count)


import sys
from itertools import combinations

input = sys.stdin.readline

# carry인지 체크
def is_carry_free(numbers):
    digit_sums = [0] * max(len(str(num)) for num in numbers)
    for num in numbers:
        for i, digit in enumerate(str(num)[::-1]): # 전체를 거꾸로 가져옴 
            digit_sums[i] += int(digit)
            if digit_sums[i] >= 10: # 각 자릿수의 합이 10 이상이 되는지 체크
                return False
    return True

N = int(input())
numbers = [int(input().strip()) for _ in range(N)]

max_count = 1
for r in range(2, N + 1):
    for combo in combinations(numbers, r):
        if is_carry_free(combo):
            max_count = r
            break
    else:
        break

print(max_count)