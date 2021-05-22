# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def trans_num(mylistnode: ListNode):
            cnt = 0

            while mylistnode and mylistnode.val == 0:
                cnt += 1
                mylistnode = mylistnode.next
            i = 0
            j = 0
            while mylistnode:
                i = i * 10 + mylistnode.val
                mylistnode = mylistnode.next
            while i:
                j = j * 10 + i % 10
                i //= 10
            j = j * pow(10, cnt)
            return j

        num = trans_num(l1) + trans_num(l2)
        result = current = ListNode(0)
        if num == 0:
            return result
        while num:
            node = ListNode(num % 10)
            current.next = node
            num //= 10
            current = node
        return result.next

l1 = ListNode(0)
l2 = ListNode(1)
print(Solution().addTwoNumbers(l1, l2))
