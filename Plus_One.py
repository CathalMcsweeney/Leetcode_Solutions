class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while True:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
                if len(digits) < -i:
                    digits = [0]+digits
            else:
                digits[i] += 1
                return digits




solution = Solution()

digits = [1,2,3]
print(solution.plusOne(digits))
digits = [9]
print(solution.plusOne(digits))