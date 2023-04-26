def score(*scores):
    cnt=len(scores)
    average=sum(scores)/cnt
    return cnt,average
n,avg=score(95,100,90)
print(n,"과목의 평균 점수",avg,"\n")
n,avg=score(90,90,80,90)
print(n,"과목의 평균 점수",avg,"\n")

