class Solution(object):
    def length(self, head):
        count = 0
        current_node = head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        test1 = self.length(l2)
        test = self.length(l1)
        print(test)

solution = Solution()
l1 = [2,4,3]
l2 = [5,6,4]

Solution.addTwoNumbers(l1,l2)