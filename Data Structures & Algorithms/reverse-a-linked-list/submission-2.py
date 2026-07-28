# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        arr = []

        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        arrr = arr[::-1]
        ptr = head
        for i in range (len(arrr)):
            ptr.val = arrr[i]
            ptr = ptr.next
        return head