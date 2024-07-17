class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0

        words = s.split()
        lastWord = len(words)
        return len(words[lastWord-1])
    
    def lengthOfLastWord_Improved(self, s):
        length = 0
        
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
    
    def wishIThoughtOfThisFirst(self, s):
        return len(s.split()[-1])

solution = Solution()

s = "Hello World"

ss = "   fly me   to   the moon  "

print(solution.lengthOfLastWord(s))

print(solution.lengthOfLastWord_Improved(s))

print(solution.wishIThoughtOfThisFirst(ss))