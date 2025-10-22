import itertools

def solve():
    import sys
    input = sys.stdin.readline
    N= int(input())

    H = input().strip() # MOOOOO
    I = input().strip() # OOOOOO
    J = input().strip() # ABCDEF
    K = input().strip()  # UVWXYZ
    for _ in range(N): # COW,MOO,CODE ...
        T=list(input()) #[C,O,W]
        a=list(itertools.permutations([H,I,J,K],len(T)))
        found=False

        for j in a: # j= (H, I , K) or like (I ,J ,K)
            num=0
            for l in T: #C
                for k in j: # k = H, which is MOOOOO
                    if l in k: # if C in MOOOOOO
                        num+=1
                        break

            if num==len(T):
                print('Yes')
                found=True
                break
        if not found:
            print('No')
                  