def billing(dest):
 rate =dest*10
 print(rate)

s=int(input("enter the no:\n 1. avadi\n 2.retteri\n 3.central\n"))
if(s==1):
    billing(10)
elif(s==2):
    billing(30)
elif(s==3):
    billing(50)
else:
    print("invalide")         
    
    '''
enter the no:
 1. avadi
 2.retteri
 3.central
2
300
 '''
