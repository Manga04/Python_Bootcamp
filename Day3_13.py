#13. replace the elements in a array with avg of max and min element
my_list=list(map(int,input().split(" ")))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if( max < my_list[i]):
        max = my_list[i]
    elif(min > my_list[i]):
        min = my_list[i]
avg=(max+min)//2        
for i in range(len(my_list)):
        my_list[i] = avg
print(*my_list)
