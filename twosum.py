# Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.
# Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in increasing order.
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i , j
            
nums = list(map(int,input().split()))
target = int(input())
print(twosum(nums, target))