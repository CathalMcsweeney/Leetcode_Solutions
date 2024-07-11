class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = Node()
        tail = temp

        while list1 and list2:
            #print(tail.val)
            #print(list2.val)
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return temp.next
    
def LinkedList(lst):
    temp = Node()
    tail = temp
    for val in lst:
        tail.next = Node(val)
        tail = tail.next

    return temp.next
    


list1 = [1,2,4]
list2 = [1,3,4]

ll1 = LinkedList(list1)
ll2 = LinkedList(list2)

solution = Solution()
mergedList = solution.mergeTwoLists(ll1,ll2)