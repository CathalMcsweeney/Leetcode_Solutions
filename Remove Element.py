class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0

        sorted(nums)
        index = 0
        left = 0
        right = len(nums)
    
        #find index of first number
        for num in nums:
            if num == val:
                break
            else:
                ans += 1

        reCalcMid = True
        nums.sort()

        while left < right:
            #get middle of array
            if reCalcMid:
                mid = (left + right) // 2
            #if middle is equal to val make index the middle
            if val == nums[mid]:
                reCalcMid = False
                index = mid
                #checks if there is another target value before the mid point
                if mid > 0 and val == nums[mid-1]:
                    #if there is, change mid point to this new point
                    mid = mid-1
                else:
                    break
            if reCalcMid:
                if val <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1

        while True:
            if index < (len(nums)) and nums[index] == val:
                nums.pop(index)
            else:
                break

        print(ans)
        print(nums)
        return len(nums)

solution = Solution()

nums = [3,2,2,3]
nums2 = [0,1,2,2,3,0,4,2]
val = 3
val2 = 2

print(solution.removeElement(nums,val))
print(solution.removeElement(nums2,val2))