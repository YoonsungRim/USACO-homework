canvas=[]
N, U = map(int, input().split())
for _ in range(N):
    canvas.append(list(input()))

#일단 제 1사분면, 2사분면,3사분면, 4사분면으로 나누어보자
first_quad=[]
for i in range((N//2)):
    first_quad.append(canvas[i][N//2:])
second_quad=[]
for i in range((N//2)):#2사분면을 옆으로 뒤집어서 1사분면의 원래 위치(?)와 똑같게 만들자
    second_quad.append(canvas[i][:N//2][::-1])
third_quad=[]
for i in range((N//2)):
    third_quad.append(canvas[N-1-i][:N//2][::-1])
fourth_quad=[]
for i in range((N//2)):
    fourth_quad.append(canvas[N-1-i][N//2:])

#맨 처음에는 몇번 바꿔야 하는지 구하기
ans=0
for i in range(N//2):# 캔버스 길이가 4라면 0,1까지 돈다(두번)
    for j in range(N//2):
        a=[first_quad[i][j],second_quad[i][j],third_quad[i][j],fourth_quad[i][j]]
        if a.count('#')>=a.count('*'):#별이 더 적게 나왔으니 최소한 적게 바꿀려면 적게나온 별을 바꿔야 함
            ans+=a.count('*')
        elif a.count('#')<a.count('*'):
            ans+=a.count('#')
print(ans)

#(r,c)에있는 기호를 바꿨을때는 몇번 바꿔야 하는지 구하기
for _ in range(U):
    input2=list(map(int, input().split()))
    r=input2[0]-1
    c=input2[1]-1
    #1사분면
    if r < N//2 and c >= N//2:
        if first_quad[r][c-(N//2)]=='*':
            first_quad[r][c-(N//2)]='#'
        elif first_quad[r][c-(N//2)]=='#':
            first_quad[r][c-(N//2)]='*'
    #2사분면
    elif r < N//2 and c < N//2:
        if second_quad[r][c]=='*':
            second_quad[r][c]='#'
        elif second_quad[r][c]=='#':
            second_quad[r][c]='*'
    #3사분면
    elif r >= N//2 and c < N//2:
        if third_quad[r-(N//2)][c]=='*':
            third_quad[r-(N//2)][c]='#'
        elif third_quad[r-(N//2)][c]=='#':
            third_quad[r-(N//2)][c]='*'
    #4사분면
    elif r >= N//2 and c >= N//2:
        if fourth_quad[r-(N//2)][c-(N//2)]=='*':
            fourth_quad[r-(N//2)][c-(N//2)]='#'
        elif fourth_quad[r-(N//2)][c-(N//2)]=='#':
            fourth_quad[r-(N//2)][c-(N//2)]='*'
#다바꿨음
    ans=0
    for i in range(N//2):# 캔버스 길이가 4라면 0,1까지 돈다(두번)
        for j in range(N//2):
            a=[first_quad[i][j],second_quad[i][j],third_quad[i][j],fourth_quad[i][j]]
            if a.count('#')>=a.count('*'):#별이 더 적게 나왔으니 최소한 적게 바꿀려면 적게나온 별을 바꿔야 함
                ans+=a.count('*')
            elif a.count('#')<a.count('*'):
                ans+=a.count('#')
    print(ans)