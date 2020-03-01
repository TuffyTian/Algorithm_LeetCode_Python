class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1_current = l1
        l2_current = l2
        new_node = None
        new_current: ListNode = None

        temp = 0
        while l1_current or l2_current:
            d1 = l1_current.val if l1_current else 0
            d2 = l2_current.val if l2_current else 0

            if l1_current:
                l1_current = l1_current.next

            if l2_current:
                l2_current = l2_current.next

            sum = d1 + d2 + temp
            temp, new_val = divmod(sum, 10)
            # temp = sum / 10
            # newVal = sum % 10
            if new_node is None:
                new_node = ListNode(new_val)
                new_current = new_node
            else:
                new_current.next = ListNode(new_val)
                new_current = new_current.next

        if temp != 0:
            new_current.next = ListNode(1)
            new_current = new_current.next

        return new_node


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))