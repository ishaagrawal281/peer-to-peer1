# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
nums = int(input())
arr = list(map(int,input().split()))
for i in range(nums):
    for j in range(nums-i-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
print(*arr)