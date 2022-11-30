# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def makeListNode(self, num: str) -> Optional[ListNode]:
        if (len(num) > 1):
            return ListNode(num[0], self.makeListNode(num[1:]))
        else:
            return ListNode(num[0])
    
    def getNum(self, l: Optional[ListNode]) -> str:
        ans = ""
        # if (l1.next != None):
        #     return self.getNum(l1.next) + str(l1.val)
        # else:
        #     return str(l1.val)
        while l.next != None:
            ans = str(l.val) + ans
            l = l.next
        ans = str(l.val) + ans
        return ans
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(self.getNum(l1))
        num2 = int(self.getNum(l2))
        return self.makeListNode(str(num1 + num2)[::-1])
        
