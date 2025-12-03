def solution():
    firstinput = list(map(int, input().split()))  # [5,3,4]
    N = int(firstinput[0])
    K = int(firstinput[1])
    T = int(firstinput[2])
    
    cows = []  # 0부터 N-1까지 소
    for n in range(N):
        cows.append(n)
    
    secondinput=list(map(int, input().split()))  # [0,2,3]
    currentindex=[]
    currentindex=secondinput[0:]  # 복사본
    
    for _ in range(T):
        # futureindex 만들기
        temp=currentindex[0:]   # temp temporary 다름
        temp.append(currentindex[0])  # [0,2,3,0]
        futurelist=temp[1:]  # [2,3,0]
        value=cows[currentindex[0]]
        for k in range(len(futurelist)):
            futurecowindex=futurelist[k]
            temporary=cows[futurecowindex]#temporary:기존에 소가 있던 곳의 소 값을 임시로 저장
            cows[futurecowindex] = value# 나중에 갈 소의 자리에 value 할당
            value=temporary#다음 for loop에서 value가 호출됨(지금은 나중에갈 자리이지만 다음 loop에서는 현재 있는 자리가 될 것임.

        for m in range(len(currentindex)):
            currentindex[m]=(currentindex[m] + 1) % N
    
    # 결과 출력
    result=[]
    for i in range(N):
        result.append(cows[i])

    print(' '.join(map(str, result)))

solution()