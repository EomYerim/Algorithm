# n = 30 
import sys
input = sys.stdin.readline
numbers = []
for i in range(28):
        line = input()
        numbers.append(int(line))
list = list(range(1,31))
numbers.sort()
res = [x for x in list if x not in numbers]
for i in res:
    print(i)


        
