class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = currNode = ListNode()

        carryOver = quotient = 0
        while l1 and l2:
            currValue = (l1.val + l2.val + carryOver) % 10
            carryOver = (l1.val + l2.val + carryOver) // 10
            nextNode = ListNode(currValue)
            currNode.next = nextNode
            currNode = currNode.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            currValue = (l1.val + carryOver) % 10
            carryOver = (l1.val + carryOver) // 10
            nextNode = ListNode(currValue)
            currNode.next = nextNode
            currNode = currNode.next
            l1 = l1.next

        while l2 is not None:
            currValue = (l2.val + carryOver) % 10
            carryOver = (l2.val + carryOver) // 10
            nextNode = ListNode(currValue)
            currNode.next = nextNode
            currNode = currNode.next
            l2 = l2.next

        if carryOver != 0:
            nextNode = ListNode(carryOver)
            currNode.next = nextNode
            currNode = currNode.next

        return head.next
