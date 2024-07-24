#9 find the elements that is present in k+N index
# k is given by user k=3, input paramets are {3 6 8 4 61 2} and N=2
#k=3 n=4 { 80 70 54 72 } Output=error
my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
for i in range(0,len(my_list)):
       print(my_list[k+n])
       break
if( k+n > len(my_list)):
     print("error")
