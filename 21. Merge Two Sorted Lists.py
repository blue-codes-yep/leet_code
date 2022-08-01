# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node so I don't have to worry about edgecase of inserting into an empty list.
        dummy = ListNode()
        # Tail of the list is the dummy node.
        tail = dummy

        # If both of the list nodes are none empty then we can compare the two values.
        while list1 and list2:
            if list1.val < list2.val:
                # Take the list1 value, and insert it into the tail.
                tail.next = list1
                # Update list1 pointer.
                list1 = list1.next
            # Same thing but with list2.
            else:
                tail.next = list2
                list2 = list2.next
            # Update tail pointer, tail pointer is updated regardless of which node is inserted into list so doesn't have to be in conditional.
            tail = tail.next
        # Check if any list nodes are empty, and insert at the end of our results.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
