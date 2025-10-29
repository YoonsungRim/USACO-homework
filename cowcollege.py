# Solution
import sys
imput=sys.stdin.readline
N=input()# 4
Cows=list(map(int,input().split()))# 1 6 4 6
Cows.sort()# 1 4 6 6
ExpectedTotalTuition={}
cowlen=len(Cows)

for index,i in enumerate(Cows): # i=학비
    if i*(cowlen-index) in ExpectedTotalTuition:
        ExpectedTotalTuition[i*(cowlen-index)].append(i)
    else:
        ExpectedTotalTuition[i*(cowlen-index)] = [i] #이따가 key 다 받고 비교
# {4:1, 12:4, 12:6, 6:6}

TotalTuition=max(ExpectedTotalTuition.keys())# 12
ChosenTuition=min(ExpectedTotalTuition[TotalTuition])# 4 

print(TotalTuition,ChosenTuition)