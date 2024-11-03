'''Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
'''

def large_n(nums):
    max_num = max(nums) 
    max_index = nums.index(max_num)
    if all(max_num >= 2 * num for i, num in enumerate(nums) if i != max_index):
        return max_index
    else:
        return -1



print(large_n([0,0,0,1]))
    
