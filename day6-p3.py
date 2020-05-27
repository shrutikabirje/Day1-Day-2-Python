Write program to implement Insertion sort.


nums=[1,2,34,5,67,89,68]
for i in range (1,len(nums)):
    curr=nums[i]
    index=i
    while (curr<nums[index-1] and index>=0):
        nums[index]=nums[index-1]
        index=index-1
    nums[index]=curr
print(nums)
