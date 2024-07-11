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
    
    def searchInsertFaster(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < mid:
                right = nums[mid]
            else:
                left = mid + 1

        return left
    
solution = Solution()
nums = [1,3,5,6]
target = 7

print(solution.searchInsertFaster(nums, target))