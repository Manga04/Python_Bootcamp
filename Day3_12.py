#12. write the code for min element
my_list=list(map(int,input().split(" ")))
temp=my_list[0]
for i in range(0,len(my_list)):
    if( temp > my_list[i]):
       temp = my_list[i]
print(temp)
