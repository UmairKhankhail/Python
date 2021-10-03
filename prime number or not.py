num=int(input("Enter any number: "))
a=2
for i in range(2,num):
   a+=1
   if((num%i)==0):
       break

if(a==num):
    print("Prime")
else:
    print("Not Prime")