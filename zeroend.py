# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1.
n = int(input())
arr = list(map(int,input().split()))
target = int(input())
def find_target (arr,target):
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
print(find_target (arr,target))