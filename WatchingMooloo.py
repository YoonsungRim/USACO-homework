#Solution
# Solution
def solution():
    firstinput = input().split()
    N = int(firstinput[0])
    K = int(firstinput[1])
    secondinput = input().split()
    days = list(map(int, secondinput))
    result= K + 1
    for i in range(1, N):
        if days[i]-days[i-1] > K:
            result+= K + 1# 다시 구독
        elif days[i]-days[i-1] <= K:
            result+= (days[i]-days[i-1]) #계속 구독
    print(result)
solution()