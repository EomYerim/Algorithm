import sys
input= sys.stdin.readline
N = int(input())
arr =[]
res= []
cow = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy','Sue']
cow.sort()

# # "must be milked beside" 처음에 나오는 문자열이랑 가장 마지막에 나오는 문자열 기준으로 슬라이싱
for i in range(N):
     str = input().rstrip()
     A, B = (str.split(" ")[0], str.split(" ")[-1]) 
     arr.append(A)  
     arr.append(B)
print(arr)
for i in range(len(cow)) :
    if cow[i] in arr and cow[i] not in res and i!=len(cow):
        x= arr.index(cow[i]) # B인덱스 찾아서 
        res.append(cow[i])
        res.append(arr[x+1])
    else:
        res.append(cow[i])


    # for j in range(len(arr)):
    #      if i in arr :
    #           res.append(arr[j])
    #      else:
    #           if arr[i][0]>j:
    #             res.append(arr[i])
    #             res.append(j)
    #           else:
    #             res.append(j)
    #             res.append(arr[i])
                  
              
print(res)
# print(arr)
# cow_list = [i for i in cow  if i not in arr]
# cow_list.sort()
# for i in arr:
#     for j in i:
#         if j in res:
#             pass
#         else:
#             res.append(j)
#     # for k in cow_list:
#     #     if res[0]>k:
#     #         res.append(k)
#     #     else:
#     #         res.append(res[0])
#     #         res[0]=k
# print(res)
# for i in range(N):
#     str = input().rstrip()
#     A = str.split(" ")[0]
#     B = str.split(" ")[-1]
#     if B in arr:
#         x= arr.index(B) # B인덱스 찾아서 
#         if arr[x-1] > A:
#             arr.append(arr[x-1])
#             arr[x-1]=A
#         else:
#             arr.append(A)
#     else:
#         arr.append(A)
#         arr.append(B)

# print(arr)




# if arr[0]<cow_list[0]:
#     res=arr+cow_list
# else:
#      res = cow_list+arr
# for i in res:
#     print(i)

# cow_list = [i for i in cow if all(i != x for pair in arr for x in pair)]
# arr = [(min(a, b), max(a, b)) for a, b in arr]
# arr.sort()

# # 결과 리스트 초기화
# result = []

# # arr의 각 쌍을 결과에 추가
# for pair in arr:
#     if pair[0] not in result:
#         result.append(pair[0])
#     if pair[1] not in result:
#         result.append(pair[1])

# # cow_list의 소들을 적절한 위치에 삽입
# for cow in cow_list:
#     for i in range(len(result) + 1):
#         if i == len(result) or cow < result[i]:
#             result.insert(i, cow)
#             break

# # 결과 출력
# for cow in result:
#     print(cow)
          
# for i in range(N):
#     str = input().rstrip()
#     A = str.split(" ")[0]
#     B = str.split(" ")[-1]
#     if B in arr:
#         x= arr.index(B) # B인덱스 찾아서 
#         if arr[x-1] > A:
#             arr.append(arr[x-1])
#             arr[x-1]=A
#         else:
#             arr.append(A)
#     else:
#         arr.append(A)
#         arr.append(B)


# cow_list = [i for i in cow  if i not in arr]
# cow_list.sort()


# if arr[0]<cow_list[0]:
#     res=arr+cow_list
# else:
#      res = cow_list+arr
# for i in res:
#     print(i)


# from itertools import permutations

# def is_valid(order, conditions):
#     for a, b in conditions:
#         if abs(order.index(a) - order.index(b)) != 1:
#             return False
#     return True

# def solve_cow_ordering(N, conditions):
#     cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
    
#     for perm in permutations(cows):
#         if is_valid(perm, conditions):
#             return perm
    
#     return None  # 해결책이 없는 경우

# # 입력 받기
# N = int(input())
# conditions = []
# for _ in range(N):
#     condition = input().split()
#     conditions.append((condition[0], condition[5]))

# # 문제 해결
# result = solve_cow_ordering(N, conditions)

# # 결과 출력
# if result:
#     for cow in result:
#         print(cow)
# else:
#     print("No solution found.")