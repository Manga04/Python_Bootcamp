#18. sum of even digits in a num
n=int(input())
sum=0
while(n>0):
    a=n%10
    if(a%2==0):
       sum=sum+a
    n=n//10
print(sum)