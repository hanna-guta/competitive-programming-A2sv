# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
            
        x = length // k
        rem = length % k

        res = []
        curr = head
        
        for i in range(k):
            dummy = ListNode()
            curr_part = dummy
            
            part_len = x + 1 if i < rem else x

            for j in range(part_len):
                if curr:
                    curr_part.next = ListNode(curr.val)
                    curr_part = curr_part.next
                    curr = curr.next
            
            res.append(dummy.next)

        return res
