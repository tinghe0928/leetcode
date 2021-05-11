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
head = Solution().reverseList(head)


def get_len(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l


def get_ele(head, i):
    l = get_len(head)
    if i < 0 or i >= l:
        return -1
    j = 0
    while head:
        if j == i:
            return head.value
        head = head.next
        j += 1
    return j


def insert_ele(head, value, i):
    nodelist = ListNode(value)
    if i < 0:
        nodelist.next = head
        return nodelist
    elif i >= get_len(head):
        pass
    else:
        pre = head  #一定要先将head赋值出去，head会移动
        for j in range(i-1):
            head = head.next
        nodelist.next = head.next
        head.next = nodelist
    return pre


head = insert_ele(head, 5, 2)
while head:
    print(head.value)
    head = head.next





