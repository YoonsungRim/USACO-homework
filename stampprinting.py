#stampprinting
#Stamp Grid
T = int(input().strip())
for _ in range(T):
    #Paintings
    N = int(input().strip())
    for _ in range(N):
        painting = input().strip() 
    #Stamp
    K = int(input().strip())
    for _ in range(K):
        stamp = input().strip() 
# * . .
# . * .
# . . *
    
def rotate90(stamp):
    result = []
    for column in range(K):#K=스탬프 길이
        new_row = []
        for row in stamp[::-1]: 
            new_row.append(row[column])
    return result

def rotate180(stamp):
    result = [] 
    for row in stamp[::-1]:
        new_row = row[::-1]
        result.append(new_row)
    return result  

def rotate270(stamp):
    result = []
    for column in range((K),-1,-1,-1):#이번에는 뒤에서
        new_row = []
        for row in stamp[::-1]: 
            new_row.append(row[column])
    return result
