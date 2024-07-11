class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0

        for num in nums:
            if num >= target:
                return ans
            else:
                ans += 1

        print("test")

        return ans
    
solution = Solution()

nums = [1,3,5,6]
target = 7

print(solution.searchInsert(nums, target))