T = int(input())#테스트 케이스 개수
for _ in range(T):
    input()
    N = int(input())#벳씨가 원하는 그림의 크기
    grid = [list(input()) for _ in range(N)]#그림을 한줄씩 나눠서 받음
    K = int(input())#빠머존이 갖고있는 스탬프의 크기
    stamp = [input() for _ in range(K)]#도장을 한줄씩 나눠서 받음
    ans = [['.' for _ in range(N)] for _ in range(N)]# 도장을 찍을 도화지를 아무것도 없는 상태로 만든다
    for rot in range(4):#4가지 방향이 있다는 뜻임 (0도,90도,180도,270도)
        for i in range(N-K+1):#도장을 찍을 수 있는 가로의 범위
            for j in range(N-K+1):#도장을 찍을수 있는 세로의 범위
                if all(grid[i+a][j+b] == '*' or stamp[a][b] == '.' for a in range(K) for b in range(K)):#stamp와 도화지의 모든 부분을 돈다. 도화지에서 '.'이고, 스탬프에서 '*'이면 찍으면 안되지만, 도화지에서 '*'이고 스탬프에서 '.'이면 찍어도 된다. 이 조건을 모두 만족하면 스탬프를 찍을 수 있음.
                    for a in range(K):
                        for b in range(K):
                            if stamp[a][b] == '*':#캔버스에 찍어야 하는 부분과 스탬프가 찍어야 하는 부분이 겹친다면
                                ans[i+a][j+b] = '*'#스탬프를 찍는다
        stamp = [[stamp[j][K-1-i] for j in range(K)] for i in range(K)]#스탬프를 90도 회전시킵니다
    print("YES" if grid == ans else "NO")#똑같이 생겼으면 Yes, 아니면 No