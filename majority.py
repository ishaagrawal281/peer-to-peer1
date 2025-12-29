# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
nums = list(map(int,input().split()))
candidate = None
count = 0
for x in nums:
    if count == 0:
        candidate = x
        count = 1

    elif x == candidate:
        count += 1
    else:
        count -= 1

print(candidate)