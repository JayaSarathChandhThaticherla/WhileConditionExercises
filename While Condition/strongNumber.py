Input=int(input("enter the number"))
temp=Input
rem=1
adfact=0
while Input>0:
    rem=Input%10 # 5 
    Input=Input//10 #14 
    fact=1
    for x in range(1,rem+1):
        
        fact=fact*x #5!
    adfact=adfact+fact
if(temp==adfact):
    print("it is strong")
else:
    print("it is not")

    
    

