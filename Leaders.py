# Solution
N = int(input())# 4
s = input()# GHHG
arr = list(map(int, input().split()))# [2,4,3,4]
arr = [x - 1 for x in arr] #[1,3,2,3](1씩 뺐음)

eG, eH, lG, lH = -1, -1, -1, -1# eG,eH=G와 H의 처음위치/ lG,lH=G와 H의 마지막위치/ -1=아직 못찾았다는 뜻

for i in range(N - 1, -1, -1):# 3, 2, 1, 0
    if (s[i] == 'G'):#건지라면
        eG = i #eG=0/가장 왼쪽 인덱스
    if (s[i] == 'H'):#홀슈타인이라면
        eH = i #eH=1/가장 왼쪽 인덱스

for i in range(N):# 0,1,2,3
    if (s[i] == 'G'):#건지라면
        lG = i #lG=3/ 가장 오른쪽 인덱스
    if (s[i] == 'H'):
        lH = i #lG=2/ 가장 오른쪽 인덱스

ans = 0 #횟수? 그런거임

if (arr[eG] >= lG):# 맨 앞에 g(eG)가 g의 리더일때
    for i in range(eG): #
        if (i == eH):
            continue
        if (s[i] == 'H' and arr[i] >= eG):#만약 H가 g리더의 리더라면
            ans += 1# +1

if (arr[eH] >= lH):# 맨 앞에 H(eH)가 H의 리더일때
    for i in range(eH):
        if (i == eG):
            continue
        if (s[i] == 'G' and arr[i] >= eH):#근데 G가 리더H의 앞에 있다면
            ans += 1#+1

if ((arr[eG] >= lG or (eG <= eH and arr[eG] >= eH)) and (arr[eH] >= lH or (eH <= eG and arr[eH] >= eG))):
    ans += 1#만약 G와 H가 모두 리더 자격을 충족하면 1을 더해라

print(ans)