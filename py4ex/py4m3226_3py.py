#Find the largest number in this list (no max()):

nums = [12, 7, 25, 3, 19]
largest = nums[0]

for larg_num in nums :
   if  larg_num > largest :
       largest = larg_num

print (largest)