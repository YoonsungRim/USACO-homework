n = int(input())#소 수
s = input()

lastG = -1
secondlastG = -1
lastH = -1
secondlastH = -1

ans = 0#lonley photo 개수

for i in range(n):#소 한마리씩 받음
    if s[i] == 'G':
        secondlastG = lastG
        lastG = i#lastG는 계속 바뀔수 있으니 계속 경신시킴
    else:
        secondlastH = lastH
        lastH = i#lastH도 계속 경신시킴

    if i >= 2 and lastG != -1 and lastH != -1:#i가 >=2라는건 photo에 3마리 이상이 들어간다는 것, lastG와lastH가 -1이 아니라는건 이미 하나씩은 소 줄에 있다는거임
        if lastG <= i-3 or lastH <= i-3:#GHHH 이런거 or HGGG (lonley함)
            ans = ans + min(lastG, lastH) - min(secondlastG, secondlastH)# 이 줄에서는 lastG뒤로 뭐가있던간에 다 자르고 lastG를 포함한 lonleyphoto가 몇개 있는지 본다. GHGHGHHHH면 GHGH는 빼고 GHHHH에서 lonely photo가 몇개인지 센다.

        else:#GHG같은거
            ans = ans + (i-2) - min(secondlastG, secondlastH)# 방금 위 줄은 왼쪽부터 있던 lonleyphoto를 셌다면, 이 줄은 오른쪽부터 lonleyphoto를 센다.

print(ans)