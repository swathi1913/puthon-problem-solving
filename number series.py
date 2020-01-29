s=int(input("enter the no:\n1:odd\n2:even\n3:div by 3\n4:div by 5\n"))
if(s==1):
    for i in range(1,20):
        if(i%2!=0):
            print(i)
elif(s==2):
    for i in range(2,20):
        if(i%2==0):
            print(i)
elif(s==3):
    for i in range(1,20):
        if(i%3==0):
            print(i)
elif(s==4):
    for i in range(1,20):
        if(i%5==0):
            print(i)
            

