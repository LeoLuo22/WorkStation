# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if(head == None):
            return None
        if(head.next == None):
            return head
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head

        return tmp

