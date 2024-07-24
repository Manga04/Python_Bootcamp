#14. find the missing nnumber in an array 
#my_list=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
exp_sum=0
for i in range(1,len(n)+2):
        exp_sum += i
act_sum=0        
for j in n:
    act_sum += j
miss = exp_sum-act_sum  
print(miss)
