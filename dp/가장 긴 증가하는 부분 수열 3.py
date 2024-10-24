import sys

N = int(input())
arr = list(map(int,input().split()))

def binary_search(arr,target):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if (arr[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return start

res=[arr[0]]
for i in range(1,len(arr)):
    if arr[i]>res[-1]:
        res.append(arr[i])
    else:
        index=binary_search(res,arr[i])
        res[index]=arr[i]
print(len(res))