#15. find the duplicates in an array-----O(n)
my_list=list(map(int,input().split()))
new_list=[]
for i in my_list:
    if( i not in new_list ):
        new_list.append(i)
print(*new_list)