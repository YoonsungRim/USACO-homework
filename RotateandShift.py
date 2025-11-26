def solution():
    firstinput = list(map(int, input().split()))# [5,3,4]
    N = int(firstinput[0])
    K = int(firstinput[1])
    T = int(firstinput[2])
    cows=[]#1부터,5까지
    for n in range(N):
        cows.append(n) #소를 0부터 4(5-1)까지 넣기
    secondinput = list(map(int, input().split()))# [0,2,3] 움직일 k마리 소들의 위치
    currentindex=[]
    for i in secondinput:
        currentindex.append(i)#복사본을 만든다.       움직일 소들의 위치 [0,2,3]
    secondinput.append(secondinput[0])# [0,2,3] >> [0,2,3,0] 3에 있던 소가 0으로 가야하는데 다음 리스트에 정해진게 없음
    del secondinput[0]# [2,3,0] 이건 지금 소가 움직여야 하는 위치를 알려주는 리스트임
    futureindex=secondinput#[2,3,0]             소가 움직일 위치
    
    for _ in range(T):#4분이니 4번 반복
        for k in range(len(futureindex)):# 이 반복문 안에서는 세마리의 소가 이동을 할것이다.
            currentcow=cows[currentindex[k]]#움직일 소의 위치이자 그 소의 번호     ( 0 )
            nextcow=cows[futureindex[k]]#움직일 소가 나중에 갈 위치이자 그 소의 번호 ( 2 )
            nextcow=currentcow
        for m in range(len(currentindex)):
            currentindex[m]+=1#움직일 소들을 새로 옆에 있는 소로 바꾸기 위해 인덱스를 1 더한다.
    print(cows)
solution()