def solve():
    import sys
    input = sys.stdin.readline
    
    die1win=0
    die2win=0

    T = int(input())
    die1= int(input())
    die2= int(input())

    for i in die1:
        for j in die2:
            if i > j:
                die1win += 1
            elif i < j:
                die2win += 1
            elif i == j:
                pass
    

    if die1win > die2win: #A > B / B > C / C > A
        for c1 in range(1, 11):
            for c2 in range(1, 11):
                for c3 in range(1, 11):
                    for c4 in range(1, 11):
                        ListC = [c1, c2, c3, c4]
                    #C가 A보다 약하고  //  C가 B보다 강한지 확인
                        dieAwin=0
                        dieCwin=0
                        for i in die1:
                            for j in ListC:
                                if i > j:
                                    dieAwin+=1
                                elif i < j:
                                    dieCwin+=1
                                elif i == j:
                                    pass
                        
                        if dieCwin > dieAwin:
                            dieBwin=0
                            dieCwin=0
                            for i in ListC:
                                for j in die2:
                                    if i > j:
                                        dieCwin+=1
                                    elif i < j:
                                        dieBwin+=1
                                    elif i == j:
                                        pass

                            if dieBwin > dieCwin:
                                return ('yes')
                            else:
                                return ('no')
                            

    elif die2win > die1win: # B > A / A > C / C > B
        for c1 in range(1, 11):
            for c2 in range(1, 11):
                for c3 in range(1, 11):
                    for c4 in range(1, 11):
                        ListC = [c1, c2, c3, c4]
                    #C가 A보다 약하고  //  C가 B보다 강한지 확인
                        dieBwin=0
                        dieCwin=0
                        for i in die1:
                            for j in ListC:
                                if i > j:
                                    dieBwin+=1
                                elif i < j:
                                    dieCwin+=1
                                elif i == j:
                                    pass
                        
                        if dieCwin > dieBwin:
                            dieAwin=0
                            dieCwin=0
                            for i in ListC:
                                for j in die2:
                                    if i > j:
                                        dieCwin+=1
                                    elif i < j:
                                        dieAwin+=1
                                    elif i == j:
                                        pass

                            if dieAwin > dieCwin:
                                return ('yes')
                            else:
                                return ('no')