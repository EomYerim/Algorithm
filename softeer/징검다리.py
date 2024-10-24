# 처음 제출한 틀린 코드 
# import sys
# N = int(input())
# stone = list(map(int,input().split()))
# temp=stone[0]
# cnt=1
# for i in range(1,len(stone)):
#     if temp <=stone[i]:
#         temp = stone[i]
#         cnt+=1
# print(cnt)


# LIS (최장 증가 수열) 문제 , 이분 탐색
import sys
N = int(input())
stone = list(map(int,input().split()))

def binary_search(stone,target):
    start,end=0,len(stone)-1 # 시작과 끝
    while start<=end: 
        mid=(start+end)//2 # 중간값 탐색
        if stone[mid]<target:
            start=mid+1 # target값이 더 크다면 오른쪽 값 기준으로 
        else:
            end = mid-1 #target 값이 더 작다면 왼쪽 값 기준으로
    return start


lis = [stone[0]] # 첫번째 탐색 값
for i in range(1,len(stone)):
    if stone[i]>lis[-1]: # 이진탐색은 정렬 된 값 기준으로 탐색
        lis.append(stone[i])
    else:
        index=binary_search(lis,stone[i])
        lis[index]=stone[i]
print(len(lis))
