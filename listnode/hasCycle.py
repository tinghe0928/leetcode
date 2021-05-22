# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        res = {}
        while head:
            if head not in res:
                res[head] = head.val
                head = head.next
            else:
                return True
        return False
