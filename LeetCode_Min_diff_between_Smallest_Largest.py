class Solution(object):
   
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, removing 3 leaves at most 1 element, so the difference is 0
        
        nums.sort()  # Sort the list to make finding differences easier
        
        # Calculate the differences for the four combinations
        diff1 = nums[-1] - nums[3]   # Remove the first 3 elements
        diff2 = nums[-4] - nums[0]   # Remove the last 3 elements
        diff3 = nums[-2] - nums[2]   # Remove the first 1 and last 2 elements
        diff4 = nums[-3] - nums[1]   # Remove the first 2 and last 1 elements
        
        # Return the minimum of these differences
        return min(diff1, diff2, diff3, diff4)



solution = Solution()
nums = [0,0,0,3,4,6,6,6]    
nums2 = [1, 3, 5, 7, 9]

#print(solution.minDifference(nums2))
print(solution.minDifference(nums))
