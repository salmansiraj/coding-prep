class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        ptr = head
#         self.displayList(head)
#         print('-----')

        while (ptr is not None):
            if ptr.child is None:
                ptr = ptr.next
            else:
                tail = self.flattenNode(ptr.child)
                tail.next = ptr.next
                if ptr.next is not None:
                    ptr.next.prev = tail
                ptr.next = ptr.child
                ptr.child.prev = ptr
                ptr.child = None
                ptr = ptr.next

        # self.displayList(head)
        return head

    def displayList(self, node):
        while node is not None:
            print(node.val)
            node = node.next

    def flattenNode(self, node):
        ptr = node
        while (ptr.next is not None):
            ptr = ptr.next
        return ptr


# BETTER SOLUTION

# Recursively

def recursively():
    return


# Iteratively
def iteratively():
    return
