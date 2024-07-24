#reverse the number----123=321
n=int(input())
rev="" #empty string
while(n>0):
    a=n%10
    rev=rev+str(a) 
    n=n//10
print(int(rev))
