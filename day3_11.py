#*****11. find the max element in a given list-------tc=O(n)
# 12 23 36 44 45 57----
#val=my_list.sort()------ no sort function as tc of sort is O(nlogn)
my_list=list(map(int,input().split(" ")))
temp=my_list[0]
for i in range(0,len(my_list)):
    if( temp < my_list[i]):
       temp = my_list[i]
print(temp)