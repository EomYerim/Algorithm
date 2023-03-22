N = int(input())
num_list = list(map(int,input().split()))
operator = list(map(int,input().split()))
#최대,최소 값
minValue = 1e9
maxValue = -1e9
res=num_list[0]
def back(idx):
    global minValue
    global maxValue
    global res
    if idx==N:
        if minValue > res:
            minValue = res
        if maxValue < res:
            maxValue = res
        return res
    for i in range(4):
        tmp = res
        #연산자가 없을 경우
        if operator[i]==0:
            continue
        if i==0:
            res+=num_list[idx]
        elif i==1:
            res-=num_list[idx]
        elif i==2:
            res*=num_list[idx]
        else:
            #음수 처리
            if res>= 0:
               res=res//num_list[idx]
            else:
                res=(-res//num_list[idx])*-1
       
        operator[i] -= 1
        back(idx+1)
        operator[i] += 1
        res = tmp

back(1)
print(maxValue)
print(minValue)