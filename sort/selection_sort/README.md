这应该最符合人类思维的排序方法，工作原理选择排序的思路是这样的：
首先，找到数组中最小的元素，
其次，将它和数组中的第一个元素交换（如果第一个就是最小的就和自己交换）
再次，在其余元素中找到最小的元素，
再次，将它和数组中的第二个元素交换
不断重复，直到最后一个元素。

叫选择排序，是因为它不断地在其余元素中选择最小的那一个。
选择排序的移动是最少的，而交换的次数是N，其他排序算法都不具有这个性质。

稳定性：用数组实现的选择排序是不稳定的，用链表实现的选择排序是稳定的；内排序；

同样，这个算法也不行，超时
