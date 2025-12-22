with open("gymnastics.in", "r") as fin:
    K, N = map(int, fin.readline().split())

    ans=0
    total=[]
    for i in range(K):
        rank=list(map(int,fin.readline().split()))
        total.append(rank)

firstrank=total[0]
for i in firstrank:
    weakerthan_i=[]
    for j in total:
        weakercow=j[j.index(i)+1::]
        weakercow=set(weakercow)
        weakerthan_i.append(weakercow)
    weakerlist=weakerthan_i[0]
    anslist=[]
    for k in weakerthan_i[1::]:
        weakerlist=weakerlist & k
    ans+=len(weakerlist)
#print(ans)
with open("gymnastics.out", "w") as fout:
    fout.write(str(ans) + "\n")
#파일 받는거(1,2번째 줄, 23,24번째 줄)만 gpt의 힘을 좀 빌렸습니다 (나머지는 다 제가 했어요)