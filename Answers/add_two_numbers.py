class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_not_none = ListNode(0) if l1 is None else l1
        l2_not_none = ListNode(0) if l2 is None else l2
        sum = l1_not_none.val + l2_not_none.val + self.carry
        if sum > 9:
            sum -= 10
            self.carry = 1
        else:
            self.carry = 0
        node = ListNode(sum)
        if not (l1.next is None and l2.next is None):
            node.next = self.addTwoNumbers(l1_not_none.next, l2_not_none.next)
        elif self.carry == 1:
                node.next = ListNode(1)
        else:
            node.next = None
        return node
