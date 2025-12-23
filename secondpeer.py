# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
n = int(input())
arr = list(map(int,input().split()))
sorted = True
for i in range(n-1):
    if arr[i] > arr[i+1]:
        sorted = False
        break
if sorted:
    print("True")
else:
    print("False")