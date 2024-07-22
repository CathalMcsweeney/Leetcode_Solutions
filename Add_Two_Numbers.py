# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, values):
        if not values:
            self.head = None
        else:
            self.head = ListNode(values[0])
            current = self.head
            for value in values[1:]:
                current.next = ListNode(value)
                current = current.next

    def get_head(self):
        return self.head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0 
            digit2 = l2.val if l2 is not None else 0
            newDigit = digit1 + digit2 + carry
            carry = 0
            if newDigit > 9:
                carry = newDigit // 10
                newDigit = newDigit % 10

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            current.next = ListNode(newDigit)
            current = current.next

        return dummy.next
            
        
solution = Solution()

values = [9,9,9,9,9,9,9]
l1 = LinkedList(values)
l1_Head = l1.get_head()

values = [9,9,9,9]
l2 = LinkedList(values)
l2_Head = l2.get_head()

print(solution.addTwoNumbers(l1_Head, l2_Head))