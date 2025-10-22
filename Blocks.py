import itertools

def solve():
    import sys
    input = sys.stdin.readline
    N= int(input())

    H = input() # MOOOOO
    I = input() # OOOOOO
    J = input() # ABCDEF
    K = input()  # UVWXYZ
    for _ in range(N): # COW,MOO,CODE ...
        T=list(input()) #[C,O,W]
        a=list(itertools.permutations([H,I,J,K],len(T)))
        for j in a: # j= (H, I , K) or like (I ,J ,K)
            num=0
            for k in j: # k = H, which is MOOOOO
                for l in T: #C
                    if l in k: # if C in MOOOOOO
                        num+=1
                        break

        if num==len(T):
            print('Yes')
            break
        else:
            print('No')
            break
                  