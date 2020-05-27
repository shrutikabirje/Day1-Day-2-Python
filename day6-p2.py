Write program to implement Selection sort.



def sel(nums):
    n=len(nums)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if nums[j] < nums[min]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
nums=[1,4,6,3,34,56,89,99,56]
sel(nums)
print(nums)
