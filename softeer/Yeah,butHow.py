import sys
# ( ) 로만 이루어진 문자열 , ( ) 1 ,+ 로만 이루어져야 함
# 수식 중간에 공백 등 문자열 들어가면 안됨 
input=sys.stdin.readline
S=input().rstrip()
res=[]
#) ( 일때 = 괄호가 닫히고 열리는 시점에 덧셈 기호 
# () 일때는 숫자 


for i in S:
    if i=="(":
        if res and res[-1] == ")":
            res.append("+")
        
    elif res[-1]=="(" and i ==")":
        res.append("1")
    res.append(i)
print("".join(res))
