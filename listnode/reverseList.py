class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


class Solution:

    def reverseList(self, mylinkedlist):
        if mylinkedlist is None or mylinkedlist.next is None:
            return mylinkedlist
        # pre 就是那个空链表
        cur = mylinkedlist
        pre = None
        # 不断将当前链表移动到空链表上
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
head = node1
print(Solution().reverseList(head))

def get_len(head):
    l = 0

    while head:
        print(head.value)
        l += 1
        head = head.next
    print("this is the lenth of nodelist: ",l)
get_len(head)



