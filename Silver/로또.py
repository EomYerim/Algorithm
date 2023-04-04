from itertools import combinations
lotto=[]

while True:
    arr=list(map(int,input().split(" ")))
    if (arr[0]==0):
        break
    else:
        lotto.append(arr)  
        for i in range(len(lotto)):
            res=[]
            for j in combinations(lotto[i][1:],6):
                res.append(j)
            result=sorted(res)
        for i in result:
            print(*i)
        print()