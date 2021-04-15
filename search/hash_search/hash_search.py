class Solution:
    """
    哈希查找
    1. 将待查找的序列按照某种关系将齐映射成一个哈希表
    2. target也按照这种映射关系
    3. 然后在哈希表种按照这种映射关系去查找，可以节约查找成本
    """

    @staticmethod
    def insert_hash(hashtable, l, num):
        address = num % l
        while hashtable[address]:   # 当前位置已经有数据了，发生冲突,需要解决冲突
            address = (address + 1) % l
        hashtable[address] = num

    @staticmethod
    def search_hash(hashtable, l, key):
        start = address = key % l
        while hashtable[address] != key:  # 指定address对应值存在但不是关键值
            address = (address + 1) % l
            print(address)
            if hashtable[address] is None or address == start:  # 若查找到了开放单元，或者循环到了开始的位置 ，则表示没有找到
                return -1
        return address

    @staticmethod
    def hash_search(nums, key):
        l = len(nums)
        hashtable = [None for i in range(l)]
        print("初始的hashtable为：", hashtable)
        for i in range(l):
            Solution.insert_hash(hashtable, l, nums[i])
        print("哈希映射后的hashtable为：", hashtable)
        return Solution.search_hash(hashtable, l, key)


if __name__ == "__main__":
    lists = [8, 9, 10]
    key = 8
    result = Solution.hash_search(lists, key)  # 这个方法只能判断序列中有没有当前值，不能判断在第几位
    if result == -1:
        print("Ops，没有找到此值")
    else:
        print("yes,找到了,在第", result, "位呢")



