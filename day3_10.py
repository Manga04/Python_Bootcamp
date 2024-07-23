#10 print the element in a particular index, but the condi is cyclic printing
my_list=list(map(int,input().split(" ")))
k=int(input())
index = k%len(my_list)
for i in range(0,len(my_list)):
       print(my_list[index])
       break 