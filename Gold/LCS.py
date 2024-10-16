#최장 공통 부분 수열 문제
#모두의 부분 수열이 되는 수열 중 가장 긴 것

# import sys


# first_str=input()
# second_str=input()
# dp=[[[0 for i in range(len(second_str))] for _ in range(len(first_str))]]
# print(dp[0][0])

# def check(x,y):
#     if first_str[x]==second_str[x]:
#         dp[x][y]=1
#     else:
#         dp[x][y]=0
# for i in range(len(first_str)):
#     check(i,i)
# print(dp)