from llist import dllist

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        nums.sort()
        i = 0
        while i <= len(nums)-2:
            if nums[i] == nums[i+1]:
                del nums[i]
                continue
            else:
                i += 1

        print(nums)
        return len(nums)
    
    #improved version
    def removeDuplicates2(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            
        newNums = nums[:j]
        print(newNums)
        return j


solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

print(solution.removeDuplicates2(nums))
print(solution.removeDuplicates(nums))
