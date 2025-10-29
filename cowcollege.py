# Version1(using list, partially correct)
import sys
imput=sys.stdin.readline
N=input()# 4
Cows=list(map(int,input().split()))# 1 6 4 6
Cows.sort()# 1 4 6 6
ExpectedTotalTuition=[]

for index,i in enumerate(Cows): # i=학비
    ExpectedTotalTuition.append([i*len(Cows[index:]),i])
# ExpectedTotalTuition == [[4,1], [12,4], [12,6], [6,6]]
Tuitionlist=[]
for j in ExpectedTotalTuition:
    Tuitionlist.append(j[0])
MaxTuition=max(Tuitionlist)

Cowlist=[]
for k in ExpectedTotalTuition:
    if MaxTuition == k[0]:
        Cowlist.append(k[1])

TotalTuition=MaxTuition# 12
ChosenTuition=min(Cowlist)# 4 

print(TotalTuition,ChosenTuition)

#Version2(using dictionary, error)
import sys
imput=sys.stdin.readline
N=input()# 4
Cows=list(map(int,input().split()))# 1 6 4 6
Cows.sort()# 1 4 6 6
ExpectedTotalTuition={}

for index,i in enumerate(Cows): # i=학비
    ExpectedTotalTuition[i*len(Cows[index:])] = i #이따가 key 다 받고 비교
# {4:1, 12:4, 12:6, 6:6}

TotalTuition=max(ExpectedTotalTuition.keys())# 12
ChosenTuition=ExpectedTotalTuition[TotalTuition]# 4 

print(TotalTuition,ChosenTuition)