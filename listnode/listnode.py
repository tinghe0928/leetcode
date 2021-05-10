class ListNode:
    "定义单链表这种数据类型的数据结构，存在一个值和一个指针"
    def __init__(self, x):
        self.value = x
        self.next = None


class MyLinkedList:
    "定义哨兵节点"
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # 定义哨兵节点
        print("this is the head >>>>>>>>>>", self.head.value)


    def get(self, index: int) -> int:
        "当index不存在时，返回-1"
        if index < 0 or index >= self.size:
            return -1
        curr = self.head

        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, value: int) -> None:
        self.addAtIndex(0, value)

    def addAtTail(self, value: int) -> None:
        self.addAtIndex(self.size, value)

    def addAtIndex(self, index: int, value: int) -> None:
        "如果index大于链表长度或小于0，do nothing"
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size = self.size + 1
        "找到链表中要被插入的节点的位置，pred为链表的一个节点"
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(value)
        "插入节点"
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        "if the index is invalid, do nothing"
        if index < 0 or index >= self.size:
            return
        self.size =self.size - 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
        # 删除 pred.next
        pred.next = pred.next.next

node1 = MyLinkedList()

