# 2 5
# 1 2
# 5 10

input1=input()#맨 첫번째 줄 입력
deliverytimes=int(input1.split()[0]) # 2
eatingdays=int(input1.split()[1])# 5
# ^^b
for i in range(deliverytimes):# 2
    input2=input()
    date=int(input2.split()[0])# 1
    deliveredhay=int(input2.split()[1])# 2
    savedhay=deliveredhay
