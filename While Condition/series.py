inp=int(input("enter the number"))
pos=1
neg=0
i=2
while i<=inp:
    if i%2==0:
        pos=pos+i**2   
    else:
        neg=neg+i**2
    i=i+1
print(pos-neg)

     
