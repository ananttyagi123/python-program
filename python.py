#sum of n numbers:11111111+2+3+4+.....+n
num=int(input("enter the number"))
sum=0
if(num>0):
     print("sum of series=",sum)
else:
    for j in range(num,0,1):
        sum=sum+j
while(num<0):
      sum=sum+num
      num=num+1
print(sum)
